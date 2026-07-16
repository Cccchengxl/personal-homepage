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
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


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


def build_chinese_paper_insights(paper: dict[str, Any], insights: dict[str, str]) -> dict[str, str]:
    title = squash(paper.get("title", ""))
    text = " ".join([paper.get("title", ""), paper.get("abstract", ""), insights.get("discussionFocus", "")])
    matched_terms = []
    for reason in paper.get("matchReasons", []):
        if "匹配 " in reason:
            matched_terms.append(reason.split("匹配 ", 1)[1])
    if not matched_terms:
        matched_terms = [item for item in paper.get("keywords", []) if item.lower() in text.lower()][:3]
    terms_zh = "、".join(dict.fromkeys(keyword_to_zh(item) for item in matched_terms[:4]))
    if not terms_zh:
        terms_zh = "该方向的核心科学问题"

    method_zh = infer_method_zh(text)
    return {
        "articleSummaryZh": trim_text(f"该论文围绕“{title}”展开，关注{terms_zh}。作者{method_zh}，用于理解相关体系的结构、动力学或物性响应。", 420),
        "discussionFocusZh": trim_text(f"讨论重点是{terms_zh}，以及这些概念如何影响模型精度、材料性质或物理机制解释。", 420),
        "mainConclusionZh": trim_text("主要结论需要结合原文摘要和正文进一步确认；从当前元数据看，该工作给出了与上述关键词直接相关的方法、基准或物性结果。", 420),
    }


def build_paper_insights(paper: dict[str, Any]) -> dict[str, str]:
    title = squash(paper.get("title", ""))
    abstract = squash(paper.get("abstract", ""))
    sentences = split_sentences(abstract)
    reasons = paper.get("matchReasons", [])
    keywords = paper.get("keywords", [])

    if sentences:
        article_summary = " ".join(sentences[:2])
    elif abstract:
        article_summary = abstract
    else:
        article_summary = f"该论文围绕“{title}”展开，当前元数据未提供摘要。"

    focus_sentence = first_matching_sentence(sentences, [
        r"\b(propose|present|develop|introduce|construct|design)\b",
        r"\b(study|investigate|explore|analy[sz]e|examine|benchmark)\b",
        r"\b(simulat|calculat|model|method|approach|framework)\b",
    ])
    if not focus_sentence and len(sentences) > 1:
        focus_sentence = sentences[1]
    elif not focus_sentence and sentences:
        focus_sentence = sentences[0]

    matched_terms = []
    for reason in reasons:
        if "匹配 " in reason:
            matched_terms.append(reason.split("匹配 ", 1)[1])
    if not matched_terms:
        matched_terms = [item for item in keywords if item.lower() in (title + " " + abstract).lower()][:3]
    term_text = "、".join(dict.fromkeys(matched_terms[:4]))

    conclusion_sentence = first_matching_sentence(sentences, [
        r"\b(show|shows|shown|demonstrate|demonstrates|reveal|reveals|find|finds|found)\b",
        r"\b(result|results|conclude|conclusion|suggest|suggests|indicate|indicates)\b",
        r"\b(enable|enables|improve|improves|outperform|accurate|accuracy|stable|robust)\b",
    ])
    if not conclusion_sentence and sentences:
        conclusion_sentence = sentences[-1]

    discussion_focus = f"重点围绕 {term_text} 展开。" if term_text else f"重点围绕题目中的核心问题“{title}”展开。"
    if focus_sentence:
        discussion_focus = f"{discussion_focus} {focus_sentence}"

    main_conclusion = conclusion_sentence or "当前摘要未明确给出结论句，需要阅读全文进一步确认主要结论。"

    insights = {
        "articleSummary": trim_text(article_summary, 620),
        "discussionFocus": trim_text(discussion_focus, 620),
        "mainConclusion": trim_text(main_conclusion, 620),
    }
    insights.update(build_chinese_paper_insights(paper, insights))
    return insights


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
    paper.update(build_paper_insights(paper))
    return paper


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


def build_feed(config: dict[str, Any], offline: bool = False) -> dict[str, Any]:
    feed_config = config.get("paperFeed", {})
    days_back = int(feed_config.get("daysBack", 14))
    rows = int(feed_config.get("maxPerSource", 20))
    per_module_min = int(feed_config.get("minPerModule", feed_config.get("perQueryMin", 5)))
    per_module_max = int(feed_config.get("maxPerModule", feed_config.get("perQueryMax", 10)))
    user_agent = build_user_agent(config)
    mailto = feed_config.get("contactEmail") or config.get("email")
    queries = query_configs(config)

    if offline:
        return {
            "updatedAt": utc_now().isoformat(),
            "daysBack": days_back,
            "minPerModule": per_module_min,
            "maxPerModule": per_module_max,
            "status": "offline_validation",
            "notes": ["离线验证模式未访问 arXiv 或 Crossref。"],
            "modules": [
                {"name": query.get("name", "Research"), "papers": []}
                for query in queries
            ],
            "papers": [],
        }

    all_ranked: list[dict[str, Any]] = []
    modules: list[dict[str, Any]] = []
    notes = []
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

    return {
        "updatedAt": utc_now().isoformat(),
        "daysBack": days_back,
        "minPerModule": per_module_min,
        "maxPerModule": per_module_max,
        "status": "ok" if all_ranked else "no_results",
        "notes": notes,
        "modules": modules,
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
                article_summary = paper.get("articleSummaryZh") or paper.get("articleSummary")
                discussion_focus = paper.get("discussionFocusZh") or paper.get("discussionFocus")
                main_conclusion = paper.get("mainConclusionZh") or paper.get("mainConclusion")
                if article_summary:
                    lines.extend(["", f"**文章摘要：** {article_summary}"])
                if discussion_focus:
                    lines.append(f"**讨论重点：** {discussion_focus}")
                if main_conclusion:
                    lines.append(f"**主要结论：** {main_conclusion}")
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
            article_summary = paper.get("articleSummaryZh") or paper.get("articleSummary")
            discussion_focus = paper.get("discussionFocusZh") or paper.get("discussionFocus")
            main_conclusion = paper.get("mainConclusionZh") or paper.get("mainConclusion")
            if article_summary:
                lines.extend(["", f"**文章摘要：** {article_summary}"])
            if discussion_focus:
                lines.append(f"**讨论重点：** {discussion_focus}")
            if main_conclusion:
                lines.append(f"**主要结论：** {main_conclusion}")
            lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def send_email(feed: dict[str, Any], profile: dict[str, Any]) -> bool:
    host = os.environ.get("SMTP_HOST")
    port = int(os.environ.get("SMTP_PORT", "587"))
    username = os.environ.get("SMTP_USER")
    password = os.environ.get("SMTP_PASSWORD")
    mail_to = os.environ.get("MAIL_TO") or profile.get("email")
    mail_from = os.environ.get("MAIL_FROM") or username or profile.get("email")
    starttls = os.environ.get("SMTP_STARTTLS", "1") != "0"

    if not host or not mail_to or not mail_from:
        print("Email skipped: set SMTP_HOST, MAIL_TO, and MAIL_FROM/SMTP_USER to enable it.", file=sys.stderr)
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
            article_summary = paper.get("articleSummaryZh") or paper.get("articleSummary")
            discussion_focus = paper.get("discussionFocusZh") or paper.get("discussionFocus")
            main_conclusion = paper.get("mainConclusionZh") or paper.get("mainConclusion")
            if article_summary:
                lines.append(f"   文章摘要：{article_summary}")
            if discussion_focus:
                lines.append(f"   讨论重点：{discussion_focus}")
            if main_conclusion:
                lines.append(f"   主要结论：{main_conclusion}")
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
    feed = build_feed(config, offline=args.offline)

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
