#!/usr/bin/env python3
"""Fetch recent arXiv preprints and journal metadata for the homepage feed."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import smtplib
import sys
import time
from email.message import EmailMessage
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET


ARXIV_API = "https://export.arxiv.org/api/query"
CROSSREF_API = "https://api.crossref.org/works"
GOOGLE_TRANSLATE_API = "https://translate.googleapis.com/translate_a/single"
MYMEMORY_TRANSLATE_API = "https://api.mymemory.translated.net/get"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
TOP_JOURNALS = [
    "Nature",
    "Science",
    "Physical Review Letters",
    "Nature Physics",
    "Nature Materials",
    "Nature Nanotechnology",
    "Nature Chemistry",
    "Nature Computational Science",
    "Nature Communications",
    "Science Advances",
    "Proceedings of the National Academy of Sciences",
    "PNAS",
]
TOP_JOURNAL_SELECTOR_VERSION = 3
DEFAULT_TOP_JOURNAL_SEARCH_PHRASES = [
    "machine learning molecular dynamics interatomic potential thermodynamic",
    "DeepMD MACE machine learning potential",
    "strongly correlated electrons Mott Hubbard quantum spin liquid",
    "multiferroic ferroelectric magnetoelectric altermagnetism altermagnetic",
]


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_date(value: dt.datetime | dt.date) -> str:
    if isinstance(value, dt.datetime):
        return value.date().isoformat()
    return value.isoformat()


def squash(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def clean_html(value: str) -> str:
    text = re.sub(r"<[^>]+>", " ", value or "")
    return squash(text)


def read_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_json_if_exists(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (json.JSONDecodeError, OSError):
        return {}


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def write_js_assignment(path: Path, variable: str, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"window.{variable} = ")
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write(";\n")


def request_text(url: str, user_agent: str, timeout: int = 30, attempts: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(attempts):
        request = Request(url, headers={"User-Agent": user_agent})
        try:
            with urlopen(request, timeout=timeout) as response:
                return response.read().decode("utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001 - retry transient API/network failures.
            last_error = exc
            if attempt < attempts - 1:
                time.sleep(2.0 * (attempt + 1))
    assert last_error is not None
    raise last_error


def request_json(url: str, user_agent: str, timeout: int = 30) -> dict[str, Any]:
    return json.loads(request_text(url, user_agent, timeout))


def query_configs(config: dict[str, Any]) -> list[dict[str, Any]]:
    feed = config.get("paperFeed", {})
    queries = feed.get("queries") or []
    if queries:
        return queries

    fallback = []
    for area in config.get("researchAreas", []):
        fallback.append({
            "name": area.get("name", "Research"),
            "keywords": area.get("keywords", []),
            "arxivCategories": area.get("arxivCategories", []),
        })
    return fallback


def build_user_agent(config: dict[str, Any]) -> str:
    email = config.get("paperFeed", {}).get("contactEmail") or config.get("email")
    suffix = f" mailto:{email}" if email else ""
    return f"personal-homepage-paper-feed/1.0{suffix}"


def arxiv_term(keyword: str) -> str:
    keyword = keyword.replace('"', "").strip()
    if not keyword:
        return ""
    return f'all:"{keyword}"' if " " in keyword else f"all:{keyword}"


def build_arxiv_search(query: dict[str, Any]) -> str:
    keyword_terms = [arxiv_term(item) for item in query.get("keywords", []) if arxiv_term(item)]
    category_terms = [f"cat:{item}" for item in query.get("arxivCategories", []) if item]
    if keyword_terms and category_terms:
        return f"({' OR '.join(keyword_terms)}) AND ({' OR '.join(category_terms)})"
    if keyword_terms:
        return " OR ".join(keyword_terms)
    if category_terms:
        return " OR ".join(category_terms)
    return "all:science"


def fetch_arxiv(query: dict[str, Any], rows: int, user_agent: str) -> list[dict[str, Any]]:
    params = {
        "search_query": build_arxiv_search(query),
        "start": "0",
        "max_results": str(rows),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urlencode(params)}"
    root = ET.fromstring(request_text(url, user_agent))
    papers = []

    for entry in root.findall("atom:entry", ATOM_NS):
        links = entry.findall("atom:link", ATOM_NS)
        url_value = ""
        pdf_url = ""
        for link in links:
            rel = link.attrib.get("rel")
            href = link.attrib.get("href", "")
            title = link.attrib.get("title")
            if rel == "alternate":
                url_value = href
            if title == "pdf":
                pdf_url = href

        authors = [
            squash(author.findtext("atom:name", default="", namespaces=ATOM_NS))
            for author in entry.findall("atom:author", ATOM_NS)
        ]
        categories = [item.attrib.get("term", "") for item in entry.findall("atom:category", ATOM_NS)]

        papers.append({
            "source": "arXiv",
            "query": query.get("name", "Research"),
            "title": squash(entry.findtext("atom:title", default="", namespaces=ATOM_NS)),
            "authors": [item for item in authors if item],
            "abstract": squash(entry.findtext("atom:summary", default="", namespaces=ATOM_NS)),
            "published": squash(entry.findtext("atom:published", default="", namespaces=ATOM_NS)),
            "updated": squash(entry.findtext("atom:updated", default="", namespaces=ATOM_NS)),
            "url": url_value or pdf_url,
            "pdfUrl": pdf_url,
            "doi": squash(entry.findtext("arxiv:doi", default="", namespaces=ATOM_NS)),
            "venue": ", ".join([item for item in categories if item][:3]),
            "keywords": query.get("keywords", []),
        })
    return papers


def crossref_date(item: dict[str, Any]) -> str:
    for key in ("published-online", "published-print", "published", "created", "deposited"):
        parts = item.get(key, {}).get("date-parts")
        if parts and parts[0]:
            year, month, day = (parts[0] + [1, 1])[:3]
            try:
                return dt.date(int(year), int(month), int(day)).isoformat()
            except ValueError:
                continue
    return ""


def crossref_authors(item: dict[str, Any]) -> list[str]:
    authors = []
    for author in item.get("author", [])[:12]:
        name = squash(" ".join([author.get("given", ""), author.get("family", "")]))
        if name:
            authors.append(name)
    return authors


def fetch_crossref(query: dict[str, Any], rows: int, days_back: int, user_agent: str, mailto: str | None) -> list[dict[str, Any]]:
    start_date = iso_date(utc_now() - dt.timedelta(days=days_back))
    params = {
        "query": " ".join(query.get("keywords", [])) or query.get("name", "science"),
        "filter": f"from-pub-date:{start_date},type:journal-article",
        "sort": "published",
        "order": "desc",
        "rows": str(rows),
        "select": "DOI,title,author,abstract,published,published-online,published-print,created,deposited,container-title,URL,subject",
    }
    if mailto:
        params["mailto"] = mailto
    url = f"{CROSSREF_API}?{urlencode(params)}"
    payload = request_json(url, user_agent)
    papers = []

    for item in payload.get("message", {}).get("items", []):
        title = squash((item.get("title") or [""])[0])
        if not title:
            continue
        venue = squash((item.get("container-title") or [""])[0])
        papers.append({
            "source": "Journal",
            "query": query.get("name", "Research"),
            "title": title,
            "authors": crossref_authors(item),
            "abstract": clean_html(item.get("abstract", "")),
            "published": crossref_date(item),
            "url": item.get("URL", ""),
            "doi": item.get("DOI", ""),
            "venue": venue,
            "subjects": item.get("subject", []),
            "keywords": query.get("keywords", []),
        })
    return papers


def top_journal_config(config: dict[str, Any]) -> dict[str, Any]:
    feed = config.get("paperFeed", {})
    top = feed.get("topJournalFeed") or {}
    return {
        "enabled": top.get("enabled", True),
        "daysBack": int(top.get("daysBack", 180)),
        "maxPapers": int(top.get("maxPapers", 12)),
        "rowsPerPhrase": int(top.get("rowsPerPhrase", 20)),
        "archiveMonths": int(top.get("archiveMonths", 12)),
        "journals": top.get("journals") or TOP_JOURNALS,
        "searchPhrases": top.get("searchPhrases") or DEFAULT_TOP_JOURNAL_SEARCH_PHRASES,
    }


def journal_matches_top_venue(venue: str, journals: list[str]) -> str:
    venue_l = squash(venue).lower()
    if not venue_l:
        return ""
    for journal in journals:
        journal_l = squash(journal).lower()
        if journal_l in {"nature", "science", "pnas"}:
            if venue_l == journal_l:
                return journal
            continue
        if venue_l == journal_l or venue_l.startswith(f"{journal_l} ") or journal_l in venue_l:
            return journal
    return ""


def fetch_top_journal_crossref(
    phrase: str,
    rows: int,
    days_back: int,
    journals: list[str],
    user_agent: str,
    mailto: str | None,
) -> list[dict[str, Any]]:
    start_date = iso_date(utc_now() - dt.timedelta(days=days_back))
    params = {
        "query": phrase,
        "filter": f"from-pub-date:{start_date},type:journal-article",
        "sort": "published",
        "order": "desc",
        "rows": str(rows),
        "select": "DOI,title,author,abstract,published,published-online,published-print,created,deposited,container-title,URL,subject",
    }
    if mailto:
        params["mailto"] = mailto
    url = f"{CROSSREF_API}?{urlencode(params)}"
    payload = request_json(url, user_agent)
    papers = []

    for item in payload.get("message", {}).get("items", []):
        title = squash((item.get("title") or [""])[0])
        venue = squash((item.get("container-title") or [""])[0])
        matched_venue = journal_matches_top_venue(venue, journals)
        if not title or not matched_venue:
            continue
        paper = {
            "source": "Top Journal",
            "query": "顶刊相关论文",
            "title": title,
            "authors": crossref_authors(item),
            "abstract": clean_html(item.get("abstract", "")),
            "published": crossref_date(item),
            "url": item.get("URL", ""),
            "doi": item.get("DOI", ""),
            "venue": venue or matched_venue,
            "subjects": item.get("subject", []),
            "keywords": [phrase],
        }
        paper["topJournal"] = matched_venue
        paper["topJournalSearchPhrase"] = phrase
        papers.append(paper)
    return papers


def fetch_top_journal_for_venue(
    journal: str,
    query_text: str,
    rows: int,
    days_back: int,
    journals: list[str],
    keywords: list[str],
    user_agent: str,
    mailto: str | None,
) -> list[dict[str, Any]]:
    start_date = iso_date(utc_now() - dt.timedelta(days=days_back))
    params = {
        "query.container-title": journal,
        "query": query_text,
        "filter": f"from-pub-date:{start_date},type:journal-article",
        "sort": "published",
        "order": "desc",
        "rows": str(rows),
        "select": "DOI,title,author,abstract,published,published-online,published-print,created,deposited,container-title,URL,subject",
    }
    if mailto:
        params["mailto"] = mailto
    url = f"{CROSSREF_API}?{urlencode(params)}"
    payload = request_json(url, user_agent, timeout=25)
    papers = []

    for item in payload.get("message", {}).get("items", []):
        title = squash((item.get("title") or [""])[0])
        venue = squash((item.get("container-title") or [""])[0])
        matched_venue = journal_matches_top_venue(venue, journals)
        if not title or not matched_venue:
            continue
        paper = {
            "source": "Top Journal",
            "query": "顶刊相关论文",
            "title": title,
            "authors": crossref_authors(item),
            "abstract": clean_html(item.get("abstract", "")),
            "published": crossref_date(item),
            "url": item.get("URL", ""),
            "doi": item.get("DOI", ""),
            "venue": venue or matched_venue,
            "subjects": item.get("subject", []),
            "keywords": keywords,
        }
        paper["topJournal"] = matched_venue
        paper["topJournalSearchPhrase"] = query_text
        papers.append(paper)
    return papers


def parse_date(value: str) -> dt.datetime | None:
    if not value:
        return None
    value = value.replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed
    except ValueError:
        try:
            return dt.datetime.fromisoformat(f"{value}T00:00:00+00:00")
        except ValueError:
            return None


def trim_text(value: str, limit: int = 520) -> str:
    value = squash(value)
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip(" ,.;:") + "..."


def split_sentences(value: str) -> list[str]:
    text = squash(value)
    if not text:
        return []
    pieces = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'($])", text)
    return [item.strip() for item in pieces if len(item.strip()) > 20]


def first_matching_sentence(sentences: list[str], patterns: list[str]) -> str:
    for pattern in patterns:
        regex = re.compile(pattern, re.IGNORECASE)
        for sentence in sentences:
            if regex.search(sentence):
                return sentence
    return ""


TRANSLATION_CACHE: dict[str, str] = {}


def contains_cjk(value: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in value)


def translation_chunks(value: str, limit: int = 1200) -> list[str]:
    sentences = split_sentences(value) or [squash(value)]
    chunks: list[str] = []
    current = ""
    for sentence in sentences:
        if not sentence:
            continue
        if current and len(current) + len(sentence) + 1 > limit:
            chunks.append(current)
            current = sentence
        else:
            current = f"{current} {sentence}".strip()
    if current:
        chunks.append(current)
    return chunks


def translate_chunk_google(chunk: str) -> str:
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": "zh-CN",
        "dt": "t",
        "q": chunk,
    }
    url = f"{GOOGLE_TRANSLATE_API}?{urlencode(params)}"
    payload = json.loads(request_text(url, "personal-homepage-translate/1.0", timeout=5, attempts=1))
    return squash("".join(
        part[0]
        for part in payload[0]
        if isinstance(part, list) and part and part[0]
    ))


def translate_chunk_mymemory(chunk: str) -> str:
    params = {
        "q": chunk,
        "langpair": "en|zh-CN",
    }
    url = f"{MYMEMORY_TRANSLATE_API}?{urlencode(params)}"
    payload = json.loads(request_text(url, "personal-homepage-translate/1.0", timeout=10, attempts=1))
    return squash(payload.get("responseData", {}).get("translatedText", ""))


def translate_to_zh(value: str) -> str:
    text = squash(value)
    if not text:
        return ""
    if contains_cjk(text):
        return text
    cached = TRANSLATION_CACHE.get(text)
    if cached is not None:
        return cached

    translated_chunks = []
    failed_chunks = 0
    for chunk in translation_chunks(text, limit=600)[:4]:
        try:
            translated = translate_chunk_google(chunk)
            if not translated:
                translated = translate_chunk_mymemory(chunk)
            translated_chunks.append(translated)
            time.sleep(0.05)
        except Exception as exc:  # noqa: BLE001 - translation must not break the scheduled update.
            try:
                translated = translate_chunk_mymemory(chunk)
                if translated:
                    translated_chunks.append(translated)
                    time.sleep(0.05)
                    continue
            except Exception as fallback_exc:  # noqa: BLE001
                print(f"Fallback translation chunk skipped: {fallback_exc}", file=sys.stderr)
            failed_chunks += 1
            print(f"Translation chunk skipped: {exc}", file=sys.stderr)
            if not translated_chunks:
                break

    result = squash(" ".join(translated_chunks))
    if result and failed_chunks:
        result = f"{result}（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）"
    TRANSLATION_CACHE[text] = result
    return result


KEYWORD_ZH = {
    "machine learning interatomic potential": "机器学习原子间势",
    "machine learning molecular dynamics": "机器学习分子动力学",
    "molecular dynamics": "分子动力学",
    "neural network potential": "神经网络势",
    "deep potential molecular dynamics": "深度势分子动力学",
    "DeepMD": "DeepMD",
    "DeePMD-kit": "DeePMD-kit",
    "MACE potential": "MACE 势函数",
    "thermodynamic properties": "热力学性质",
    "free energy": "自由能",
    "thermal conductivity": "热导率",
    "phase transition": "相变",
    "strongly correlated systems": "强关联体系",
    "strongly correlated electrons": "强关联电子",
    "Hubbard model": "Hubbard 模型",
    "Mott insulator": "Mott 绝缘体",
    "quantum spin liquid": "量子自旋液体",
    "unconventional superconductivity": "非常规超导",
    "high-temperature superconductivity": "高温超导",
    "heavy fermion": "重费米子",
    "dynamical mean field theory": "动力学平均场理论",
    "density matrix renormalization group": "密度矩阵重整化群",
    "tensor network": "张量网络",
    "quantum many-body": "量子多体",
    "multiferroic": "多铁性",
    "multiferroic materials": "多铁材料",
    "magnetoelectric coupling": "磁电耦合",
    "ferroelectricity": "铁电性",
    "ferromagnetism": "铁磁性",
    "spin-lattice coupling": "自旋-晶格耦合",
    "交变磁性": "交变磁性",
    "altermagnetism": "交变磁性",
    "altermagnetic": "交变磁性",
    "altermagnet": "交变磁性",
    "altermagnetic materials": "交变磁性材料",
}


def keyword_to_zh(keyword: str) -> str:
    lowered = keyword.lower()
    for source, target in KEYWORD_ZH.items():
        if source.lower() == lowered:
            return target
    return keyword


def infer_method_zh(text: str) -> str:
    lowered = text.lower()
    if "first-principles" in lowered or "density functional" in lowered or "dft" in lowered:
        return "结合第一性原理或电子结构计算开展分析"
    if "benchmark" in lowered:
        return "通过系统基准测试比较模型或方法表现"
    if "molecular dynamics" in lowered or "finite-temperature" in lowered:
        return "利用分子动力学或有限温度模拟检验体系行为"
    if "propose" in lowered or "introduce" in lowered or "develop" in lowered:
        return "提出并验证新的模型、方法或工作流"
    if "measure" in lowered or "experiment" in lowered:
        return "通过实验测量或表征分析关键物性"
    return "基于摘要中的模型、计算或实验结果展开研究"


def matched_terms_for_paper(paper: dict[str, Any], text: str) -> list[str]:
    matched_terms = []
    for reason in paper.get("matchReasons", []):
        if "匹配 " in reason:
            matched_terms.append(reason.split("匹配 ", 1)[1])
    if not matched_terms:
        text_l = text.lower()
        matched_terms = [
            item for item in paper.get("keywords", [])
            if isinstance(item, str) and item.lower() in text_l
        ][:4]
    return list(dict.fromkeys(matched_terms))


def discussion_aspect_zh(text: str) -> str:
    lowered = text.lower()
    if "altermagnet" in lowered:
        return "交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应"
    if "multiferroic" in lowered or "ferroelectric" in lowered or "magnetoelectric" in lowered:
        return "极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约"
    if "hubbard" in lowered or "mott" in lowered or "strongly correlated" in lowered:
        return "有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号"
    if "benchmark" in lowered or "compare" in lowered or "outperform" in lowered:
        return "基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍"
    if "free energy" in lowered or "thermodynamic" in lowered or "phase diagram" in lowered:
        return "自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质"
    if "molecular dynamics" in lowered or "finite-temperature" in lowered or "thermal conductivity" in lowered:
        return "模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性"
    if "first-principles" in lowered or "density functional" in lowered or "dft" in lowered or "berry" in lowered:
        return "第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系"
    if "propose" in lowered or "introduce" in lowered or "develop" in lowered or "framework" in lowered:
        return "新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限"
    if "experiment" in lowered or "measure" in lowered or "spectroscop" in lowered:
        return "样品制备、实验表征条件、关键观测信号，以及这些信号如何支撑物理机制解释"
    return "研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系"


def build_discussion_focus_zh(paper: dict[str, Any], sentences: list[str], matched_terms: list[str]) -> str:
    text = " ".join([paper.get("title", ""), paper.get("abstract", "")])
    focus_sentences = []
    for patterns in [
        [r"\b(propose|present|develop|introduce|construct|design)\b"],
        [r"\b(study|investigate|explore|analy[sz]e|examine|benchmark)\b"],
        [r"\b(simulat|calculat|model|method|approach|framework|measure|experiment)\b"],
    ]:
        sentence = first_matching_sentence(sentences, patterns)
        if sentence and sentence not in focus_sentences:
            focus_sentences.append(sentence)
    if not focus_sentences and sentences:
        focus_sentences.append(sentences[0])
    if len(focus_sentences) < 2 and len(sentences) > 1:
        for sentence in sentences[1:]:
            if sentence not in focus_sentences:
                focus_sentences.append(sentence)
                break

    translated_focus = translate_to_zh(" ".join(focus_sentences[:2]))
    terms_zh = "、".join(dict.fromkeys(keyword_to_zh(item) for item in matched_terms[:4]))
    aspect = discussion_aspect_zh(text)

    parts = []
    if translated_focus:
        parts.append(translated_focus)
    elif focus_sentences:
        parts.append("可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。")
    if terms_zh:
        parts.append(f"结合关键词看，阅读时应重点关注{terms_zh}相关的{aspect}。")
    else:
        parts.append(f"阅读时应重点关注{aspect}。")
    return trim_text(" ".join(parts), 900)


def build_paper_insights(paper: dict[str, Any]) -> dict[str, str]:
    title = squash(paper.get("title", ""))
    abstract = squash(paper.get("abstract", ""))
    sentences = split_sentences(abstract)
    reasons = paper.get("matchReasons", [])
    keywords = paper.get("keywords", [])

    abstract_zh = translate_to_zh(abstract)
    if not abstract_zh and abstract:
        abstract_zh = f"自动翻译暂不可用，以下为原文摘要：{abstract}"
    elif not abstract_zh:
        abstract_zh = f"当前元数据未提供原文摘要。论文题目为“{title}”。"

    focus_sentence = first_matching_sentence(sentences, [
        r"\b(propose|present|develop|introduce|construct|design)\b",
        r"\b(study|investigate|explore|analy[sz]e|examine|benchmark)\b",
        r"\b(simulat|calculat|model|method|approach|framework)\b",
    ])
    if not focus_sentence and len(sentences) > 1:
        focus_sentence = sentences[1]
    elif not focus_sentence and sentences:
        focus_sentence = sentences[0]

    matched_terms = matched_terms_for_paper(paper, title + " " + abstract)
    term_text = "、".join(dict.fromkeys(matched_terms[:4]))

    discussion_focus = f"重点围绕 {term_text} 展开。" if term_text else f"重点围绕题目中的核心问题“{title}”展开。"
    if focus_sentence:
        discussion_focus = f"{discussion_focus} {focus_sentence}"

    insights = {
        "abstractOriginal": abstract,
        "abstractZh": trim_text(abstract_zh, 1800),
        "articleSummary": abstract,
        "articleSummaryZh": trim_text(abstract_zh, 1800),
        "discussionFocus": trim_text(discussion_focus, 620),
        "discussionFocusZh": build_discussion_focus_zh(paper, sentences, matched_terms),
    }
    return insights


def refresh_paper_insights(paper: dict[str, Any]) -> dict[str, Any]:
    paper.pop("mainConclusion", None)
    paper.pop("mainConclusionZh", None)
    paper.update(build_paper_insights(paper))
    return paper


def score_paper(paper: dict[str, Any]) -> dict[str, Any]:
    title = paper.get("title", "")
    abstract = paper.get("abstract", "")
    venue = paper.get("venue", "")
    keywords = paper.get("keywords", [])
    title_l = title.lower()
    abstract_l = abstract.lower()
    score = 0.0
    reasons = []
    keyword_matches = 0

    for keyword in keywords:
        key = keyword.lower().strip()
        if not key:
            continue
        if key in title_l:
            score += 7
            keyword_matches += 1
            reasons.append(f"标题匹配 {keyword}")
        elif key in abstract_l:
            score += 3
            keyword_matches += 1
            reasons.append(f"摘要匹配 {keyword}")
        elif key in venue.lower():
            score += 2
            keyword_matches += 1
            reasons.append(f"来源匹配 {keyword}")

    if paper.get("topJournal") and paper.get("topJournalSearchPhrase"):
        score += 6
        reasons.append(f"顶刊来源 {paper['topJournal']}")
        if keyword_matches == 0:
            keyword_matches += 1
            score += 3
            reasons.append(f"顶刊检索匹配 {paper['topJournalSearchPhrase']}")

    published = parse_date(paper.get("published", ""))
    if published:
        age_days = max(0, (utc_now() - published.astimezone(dt.timezone.utc)).days)
        score += max(0, 10 - min(age_days, 10))
        if age_days <= 3:
            reasons.append("最近 3 天发布")
        elif age_days <= 14:
            reasons.append("近两周发布")

    if paper.get("source") == "arXiv":
        score += 1

    paper["score"] = round(score, 2)
    paper["keywordMatches"] = keyword_matches
    paper["matchReasons"] = reasons[:4]
    return refresh_paper_insights(paper)


def dedupe_key(paper: dict[str, Any]) -> str:
    doi = paper.get("doi")
    if doi:
        return f"doi:{doi.lower()}"
    url = paper.get("url", "")
    arxiv_match = re.search(r"arxiv\.org/abs/([^?#]+)", url)
    if arxiv_match:
        return f"arxiv:{arxiv_match.group(1).lower()}"
    title = re.sub(r"[^a-z0-9]+", "", paper.get("title", "").lower())
    return f"title:{title[:120]}"


def dedupe_and_rank(papers: list[dict[str, Any]], top_n: int | None = None) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for paper in papers:
        scored = score_paper(paper)
        if scored.get("keywords") and not scored.get("keywordMatches"):
            continue
        key = dedupe_key(scored)
        existing = merged.get(key)
        if existing is None or scored.get("score", 0) > existing.get("score", 0):
            merged[key] = scored
        elif existing:
            existing["matchReasons"] = list(dict.fromkeys(existing.get("matchReasons", []) + scored.get("matchReasons", [])))[:4]

    def sort_key(item: dict[str, Any]) -> tuple[float, str]:
        return (float(item.get("score", 0)), item.get("published", ""))

    ranked = sorted(merged.values(), key=sort_key, reverse=True)
    return ranked[:top_n] if top_n else ranked


def clone_payload(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False))


def date_part(value: str) -> str:
    parsed = parse_date(value)
    return parsed.date().isoformat() if parsed else squash(value)[:10]


def month_part(value: str) -> str:
    parsed = parse_date(value)
    if parsed:
        return f"{parsed.year:04d}-{parsed.month:02d}"
    value = squash(value)
    return value[:7] if len(value) >= 7 else value


def flatten_module_papers(modules: list[dict[str, Any]]) -> list[dict[str, Any]]:
    papers: list[dict[str, Any]] = []
    for module in modules:
        papers.extend(module.get("papers", []))
    return papers


def previous_module_papers(previous_feed: dict[str, Any], module_name: str) -> list[dict[str, Any]]:
    for module in previous_feed.get("modules", []):
        if module.get("name") == module_name and module.get("papers"):
            return [
                refresh_paper_insights(paper)
                for paper in clone_payload(module.get("papers", []))
            ]
    return []


def update_daily_archive(previous_feed: dict[str, Any], today: str, archive_days: int) -> list[dict[str, Any]]:
    archive = clone_payload(previous_feed.get("dailyArchive") or [])
    previous_date = date_part(previous_feed.get("updatedAt", ""))
    previous_modules = [
        module for module in previous_feed.get("modules", [])
        if module.get("papers")
    ]

    if previous_date and previous_date != today and flatten_module_papers(previous_modules):
        archive = [entry for entry in archive if entry.get("date") != previous_date]
        archive.insert(0, {
            "date": previous_date,
            "label": f"{previous_date} 每日推荐",
            "description": f"自动归档的 {previous_date} 每日论文推荐。",
            "modules": clone_payload(previous_modules),
            "papers": clone_payload(flatten_module_papers(previous_modules)),
        })

    archive = sorted(archive, key=lambda item: item.get("date", ""), reverse=True)
    return archive[:archive_days]


def append_monthly_archive(
    archive: list[dict[str, Any]],
    existing: dict[str, Any],
    current_period: str,
    archive_months: int,
) -> list[dict[str, Any]]:
    existing_period = existing.get("period") or month_part(existing.get("updatedAt", ""))
    existing_papers = existing.get("papers") or []
    if existing_period and existing_period != current_period and existing_papers:
        archive = [entry for entry in archive if entry.get("date") != existing_period]
        archive.insert(0, {
            "date": existing_period,
            "label": f"{existing_period} 顶刊推荐",
            "description": f"自动归档的 {existing_period} 顶刊相关论文。",
            "papers": clone_payload(existing_papers),
        })
    archive = sorted(archive, key=lambda item: item.get("date", ""), reverse=True)
    return archive[:archive_months]


def build_top_journal_feed(
    config: dict[str, Any],
    previous_feed: dict[str, Any],
    offline: bool,
    user_agent: str,
    mailto: str | None,
    notes: list[str],
) -> dict[str, Any]:
    top_config = top_journal_config(config)
    current_period = utc_now().strftime("%Y-%m")
    existing = clone_payload(previous_feed.get("topJournal") or {})
    archive = append_monthly_archive(
        existing.get("archive") or [],
        existing,
        current_period,
        int(top_config.get("archiveMonths", 12)),
    )

    if not top_config.get("enabled", True):
        return {
            "updatedAt": existing.get("updatedAt"),
            "period": existing.get("period") or current_period,
            "selectorVersion": TOP_JOURNAL_SELECTOR_VERSION,
            "journals": top_config.get("journals", TOP_JOURNALS),
            "papers": existing.get("papers") or [],
            "archive": archive,
            "status": "disabled",
        }

    if (
        existing.get("period") == current_period
        and existing.get("papers")
        and existing.get("selectorVersion") == TOP_JOURNAL_SELECTOR_VERSION
    ):
        existing["archive"] = archive
        return existing

    if offline:
        return {
            "updatedAt": utc_now().isoformat(),
            "period": current_period,
            "selectorVersion": TOP_JOURNAL_SELECTOR_VERSION,
            "journals": top_config.get("journals", TOP_JOURNALS),
            "papers": existing.get("papers") or [],
            "archive": archive,
            "status": "offline_validation",
        }

    top_papers: list[dict[str, Any]] = []
    phrases = [item for item in top_config.get("searchPhrases", []) if item]
    journals = [item for item in top_config.get("journals", TOP_JOURNALS) if item]
    ranking_keywords = list(dict.fromkeys([
        keyword
        for query in query_configs(config)
        for keyword in query.get("keywords", [])
    ] + phrases))
    query_text = squash(top_config.get("queryText") or " ".join(phrases))
    for index, journal in enumerate(journals):
        try:
            top_papers.extend(fetch_top_journal_for_venue(
                journal,
                query_text,
                int(top_config.get("rowsPerPhrase", 20)),
                int(top_config.get("daysBack", 180)),
                journals,
                ranking_keywords,
                user_agent,
                mailto,
            ))
        except Exception as exc:  # noqa: BLE001 - monthly top-journal feed should not break daily updates.
            notes.append(f"Top-journal query failed for {journal}: {exc}")
        if index < len(journals) - 1:
            time.sleep(0.6)

    ranked = dedupe_and_rank(top_papers, int(top_config.get("maxPapers", 12)))
    if (
        not ranked
        and existing.get("period") == current_period
        and existing.get("selectorVersion") == TOP_JOURNAL_SELECTOR_VERSION
        and existing.get("papers")
    ):
        ranked = clone_payload(existing.get("papers", []))[: int(top_config.get("maxPapers", 12))]
        notes.append("Top-journal feed kept previous papers because the current query returned 0 results.")
    if not ranked:
        notes.append("Top-journal feed returned 0 papers for the configured journal list and keywords.")

    return {
        "updatedAt": utc_now().isoformat(),
        "period": current_period,
        "selectorVersion": TOP_JOURNAL_SELECTOR_VERSION,
        "daysBack": int(top_config.get("daysBack", 180)),
        "journals": journals,
        "searchPhrases": phrases,
        "papers": ranked,
        "archive": archive,
        "status": "ok" if ranked else "no_results",
    }


def build_feed(config: dict[str, Any], offline: bool = False, previous_feed: dict[str, Any] | None = None) -> dict[str, Any]:
    feed_config = config.get("paperFeed", {})
    days_back = int(feed_config.get("daysBack", 14))
    rows = int(feed_config.get("maxPerSource", 20))
    per_module_min = int(feed_config.get("minPerModule", feed_config.get("perQueryMin", 5)))
    per_module_max = int(feed_config.get("maxPerModule", feed_config.get("perQueryMax", 10)))
    archive_days = int(feed_config.get("archiveDays", 60))
    user_agent = build_user_agent(config)
    mailto = feed_config.get("contactEmail") or config.get("email")
    queries = query_configs(config)
    previous_feed = previous_feed or {}
    today = utc_now().date().isoformat()
    daily_archive = update_daily_archive(previous_feed, today, archive_days)
    notes = []

    if offline:
        top_journal = build_top_journal_feed(config, previous_feed, True, user_agent, mailto, notes)
        return {
            "updatedAt": utc_now().isoformat(),
            "daysBack": days_back,
            "minPerModule": per_module_min,
            "maxPerModule": per_module_max,
            "status": "offline_validation",
            "notes": ["离线验证模式未访问 arXiv 或 Crossref。", *notes],
            "modules": [
                {"name": query.get("name", "Research"), "papers": []}
                for query in queries
            ],
            "dailyArchive": daily_archive,
            "topJournal": top_journal,
            "papers": [],
        }

    all_ranked: list[dict[str, Any]] = []
    modules: list[dict[str, Any]] = []
    for index, query in enumerate(queries):
        query_papers: list[dict[str, Any]] = []
        try:
            query_papers.extend(fetch_arxiv(query, rows, user_agent))
        except Exception as exc:  # noqa: BLE001 - keep daily automation resilient.
            notes.append(f"arXiv query failed for {query.get('name', 'Research')}: {exc}")
        if index < len(queries) - 1:
            time.sleep(3.2)

        try:
            query_papers.extend(fetch_crossref(query, rows, days_back, user_agent, mailto))
        except Exception as exc:  # noqa: BLE001
            notes.append(f"Crossref query failed for {query.get('name', 'Research')}: {exc}")

        ranked_for_query = dedupe_and_rank(query_papers, per_module_max)
        if not ranked_for_query:
            fallback_papers = previous_module_papers(previous_feed, query.get("name", "Research"))
            if fallback_papers:
                ranked_for_query = fallback_papers[:per_module_max]
                notes.append(f"{query.get('name', 'Research')} kept previous papers because the current query returned 0 results.")
        if len(ranked_for_query) < per_module_min:
            notes.append(
                f"{query.get('name', 'Research')} returned {len(ranked_for_query)} papers; "
                f"target range is {per_module_min}-{per_module_max}."
            )
        modules.append({
            "name": query.get("name", "Research"),
            "min": per_module_min,
            "max": per_module_max,
            "papers": ranked_for_query,
        })
        all_ranked.extend(ranked_for_query)

    top_journal = build_top_journal_feed(config, previous_feed, False, user_agent, mailto, notes)

    return {
        "updatedAt": utc_now().isoformat(),
        "daysBack": days_back,
        "minPerModule": per_module_min,
        "maxPerModule": per_module_max,
        "status": "ok" if all_ranked else "no_results",
        "notes": notes,
        "modules": modules,
        "dailyArchive": daily_archive,
        "topJournal": top_journal,
        "papers": all_ranked,
    }


def write_markdown(path: Path, feed: dict[str, Any], profile: dict[str, Any]) -> None:
    lines = [
        f"# Latest papers for {profile.get('name', 'Research Feed')}",
        "",
        f"Updated: {feed.get('updatedAt')}",
        f"Window: last {feed.get('daysBack', 14)} days",
        "",
    ]
    if feed.get("notes"):
        lines.extend(["## Notes", ""])
        lines.extend([f"- {note}" for note in feed["notes"]])
        lines.append("")

    modules = feed.get("modules") or []
    if modules:
        for module in modules:
            lines.extend([f"## {module.get('name', 'Research')}", ""])
            papers = module.get("papers", [])
            if not papers:
                lines.extend(["No papers were found for this module.", ""])
                continue
            for index, paper in enumerate(papers, 1):
                authors = ", ".join(paper.get("authors", [])[:6])
                lines.extend([
                    f"### {index}. {paper.get('title', 'Untitled')}",
                    "",
                    f"- Source: {paper.get('source', '')}",
                    f"- Date: {paper.get('published', '')}",
                    f"- Venue: {paper.get('venue', '')}",
                    f"- Authors: {authors}",
                    f"- Link: {paper.get('url', '')}",
                    f"- Score: {paper.get('score', '')}",
                ])
                if paper.get("matchReasons"):
                    lines.append(f"- Match: {'; '.join(paper['matchReasons'])}")
                article_summary = paper.get("abstractZh") or paper.get("articleSummaryZh") or paper.get("articleSummary")
                discussion_focus = paper.get("discussionFocusZh") or paper.get("discussionFocus")
                if article_summary:
                    lines.extend(["", f"**中文摘要：** {article_summary}"])
                if discussion_focus:
                    lines.append(f"**讨论重点：** {discussion_focus}")
                lines.append("")
    elif not feed.get("papers"):
        lines.extend(["No papers were found for the current configuration.", ""])
    else:
        for index, paper in enumerate(feed["papers"], 1):
            authors = ", ".join(paper.get("authors", [])[:6])
            lines.extend([
                f"## {index}. {paper.get('title', 'Untitled')}",
                "",
                f"- Source: {paper.get('source', '')}",
                f"- Date: {paper.get('published', '')}",
                f"- Venue: {paper.get('venue', '')}",
                f"- Authors: {authors}",
                f"- Link: {paper.get('url', '')}",
                f"- Score: {paper.get('score', '')}",
            ])
            if paper.get("matchReasons"):
                lines.append(f"- Match: {'; '.join(paper['matchReasons'])}")
            article_summary = paper.get("abstractZh") or paper.get("articleSummaryZh") or paper.get("articleSummary")
            discussion_focus = paper.get("discussionFocusZh") or paper.get("discussionFocus")
            if article_summary:
                lines.extend(["", f"**中文摘要：** {article_summary}"])
            if discussion_focus:
                lines.append(f"**讨论重点：** {discussion_focus}")
            lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def send_email(feed: dict[str, Any], profile: dict[str, Any]) -> bool:
    host = os.environ.get("SMTP_HOST") or ""
    username = os.environ.get("SMTP_USER") or ""
    password = os.environ.get("SMTP_PASSWORD") or ""
    mail_to = os.environ.get("MAIL_TO") or profile.get("email") or ""
    mail_from = os.environ.get("MAIL_FROM") or username or profile.get("email") or ""
    starttls = (os.environ.get("SMTP_STARTTLS") or "1") != "0"

    if not host or not mail_to or not mail_from:
        print("Email skipped: set SMTP_HOST, MAIL_TO, and MAIL_FROM/SMTP_USER to enable it.", file=sys.stderr)
        return False

    try:
        port = int(os.environ.get("SMTP_PORT") or "587")
    except ValueError:
        print("Email skipped: SMTP_PORT must be a number.", file=sys.stderr)
        return False

    lines = [
        f"{profile.get('name', '你的')}每日论文推荐",
        f"Updated: {feed.get('updatedAt')}",
        "",
    ]
    modules = feed.get("modules") or [{"name": "Research", "papers": feed.get("papers", [])[:10]}]
    for module in modules:
        lines.extend([f"【{module.get('name', 'Research')}】", ""])
        for index, paper in enumerate(module.get("papers", []), 1):
            lines.extend([
                f"{index}. {paper.get('title', 'Untitled')}",
                f"   {paper.get('source', '')} | {paper.get('published', '')} | {paper.get('venue', '')}",
                f"   {paper.get('url', '')}",
            ])
            if paper.get("matchReasons"):
                lines.append(f"   Match: {'; '.join(paper['matchReasons'])}")
            article_summary = paper.get("abstractZh") or paper.get("articleSummaryZh") or paper.get("articleSummary")
            discussion_focus = paper.get("discussionFocusZh") or paper.get("discussionFocus")
            if article_summary:
                lines.append(f"   中文摘要：{article_summary}")
            if discussion_focus:
                lines.append(f"   讨论重点：{discussion_focus}")
            lines.append("")
        lines.append("")

    message = EmailMessage()
    message["Subject"] = f"每日论文推荐 · {dt.date.today().isoformat()}"
    message["From"] = mail_from
    message["To"] = mail_to
    message.set_content("\n".join(lines))

    with smtplib.SMTP(host, port, timeout=30) as smtp:
        if starttls:
            smtp.starttls()
        if username and password:
            smtp.login(username, password)
        smtp.send_message(message)
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch recent arXiv and journal papers for a personal homepage.")
    parser.add_argument("--config", default="data/profile.json", help="Path to profile and research keyword config.")
    parser.add_argument("--out", default="data/papers.json", help="Output JSON feed path.")
    parser.add_argument("--js", default="data/papers.js", help="Output browser JS feed path.")
    parser.add_argument("--profile-js", default="data/profile.js", help="Output browser JS profile path.")
    parser.add_argument("--markdown", default="data/latest-papers.md", help="Output Markdown digest path.")
    parser.add_argument("--email", action="store_true", help="Send an email digest when SMTP environment variables are set.")
    parser.add_argument("--offline", action="store_true", help="Validate output generation without network calls.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = Path(args.config)
    config = read_config(config_path)
    previous_feed = read_json_if_exists(Path(args.out))
    feed = build_feed(config, offline=args.offline, previous_feed=previous_feed)

    write_json(Path(args.out), feed)
    write_js_assignment(Path(args.js), "RESEARCH_PAPER_FEED", feed)
    write_js_assignment(Path(args.profile_js), "SITE_PROFILE", config)
    write_markdown(Path(args.markdown), feed, config)

    if args.email:
        send_email(feed, config)

    print(f"Wrote {args.out} with {len(feed.get('papers', []))} papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
