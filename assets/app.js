(function () {
  const profile = window.SITE_PROFILE || {};
  const feed = window.RESEARCH_PAPER_FEED || { papers: [] };
  const state = {
    source: "all",
    search: "",
    selectedModuleIndex: null,
    selectedEntryIndex: null,
  };

  const $ = (selector) => document.querySelector(selector);
  const create = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  };

  const setText = (selector, value) => {
    const node = $(selector);
    if (node && value) node.textContent = value;
  };

  const normalize = (value) => String(value || "").toLowerCase();

  const formatDate = (value) => {
    if (!value) return "日期待定";
    if (/^\d{4}-\d{2}$/.test(value)) return value;
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return value;
    return date.toLocaleDateString("zh-CN", { year: "numeric", month: "short", day: "numeric" });
  };

  const resetFilters = () => {
    state.search = "";
    state.source = "all";
    const search = $("#paperSearch");
    if (search) search.value = "";
    document.querySelectorAll(".filter-button").forEach((item) => {
      item.classList.toggle("active", item.dataset.source === "all");
    });
  };

  function renderTags(container, values, className) {
    container.innerHTML = "";
    values.filter(Boolean).forEach((value) => {
      container.appendChild(create("span", className, value));
    });
  }

  function renderProfile() {
    document.title = `${profile.name || "个人主页"} | ${profile.title || "Academic Portfolio"}`;
    setText("#brandName", profile.name || "个人主页");
    setText("#heroKicker", profile.kicker || "Academic Portfolio");
    setText("#heroName", profile.name || "你的姓名");
    setText("#heroSummary", profile.summary);
    setText("#profileTitle", profile.title);
    setText("#aboutText", profile.about);
    setText("#contactText", profile.contactText);
    setText("#footerName", profile.name || "个人学术主页");

    renderTags($("#heroTags"), profile.tags || [], "tag");

    const scholarLink = (profile.links || []).find((link) => /google scholar|scholar/i.test(link.label || ""));
    const heroScholar = $("#heroScholarLink");
    if (heroScholar && scholarLink && scholarLink.url) {
      heroScholar.href = scholarLink.url;
      heroScholar.hidden = false;
    } else if (heroScholar) {
      heroScholar.hidden = true;
    }

    const meta = $("#profileMeta");
    meta.innerHTML = "";
    [
      ["教育背景", profile.education],
      ["当前职位", profile.position || profile.title],
      ["机构", profile.affiliation],
      ["地点", profile.location],
      ["邮箱", profile.email],
    ].filter((item) => item[1]).forEach(([label, value]) => {
      const row = create("div", "meta-item");
      row.appendChild(create("span", "meta-label", label));
      row.appendChild(create("span", "", value));
      meta.appendChild(row);
    });

    const highlights = $("#highlightList");
    highlights.innerHTML = "";
    (profile.highlights || []).forEach((item) => highlights.appendChild(create("li", "", item)));

    const researchGrid = $("#researchGrid");
    researchGrid.innerHTML = "";
    (profile.researchAreas || []).forEach((area) => {
      const card = create("article", "research-card");
      card.appendChild(create("h3", "", area.name));
      card.appendChild(create("p", "", area.description));
      const keywords = create("div", "keyword-list");
      renderTags(keywords, area.keywords || [], "keyword");
      card.appendChild(keywords);
      researchGrid.appendChild(card);
    });

    const publications = $("#publicationList");
    publications.innerHTML = "";
    (profile.publications || []).forEach((paper) => {
      const item = create("article", "publication-item");
      item.appendChild(create("h3", "", paper.title));
      item.appendChild(create("p", "", [paper.authors, paper.venue, paper.year].filter(Boolean).join(" · ")));
      publications.appendChild(item);
    });

    const links = $("#contactLinks");
    links.innerHTML = "";
    (profile.links || []).filter((link) => link.label && link.url).forEach((link) => {
      const anchor = create("a", "", link.label);
      anchor.href = link.url;
      if (!link.url.startsWith("#") && !link.url.startsWith("mailto:")) {
        anchor.target = "_blank";
        anchor.rel = "noreferrer";
      }
      links.appendChild(anchor);
    });
  }

  function renderFeedMeta() {
    const count = (feed.papers || []).length;
    const updated = feed.updatedAt ? `更新于 ${formatDate(feed.updatedAt)}` : "等待首次更新";
    const days = feed.daysBack ? `近 ${feed.daysBack} 天` : "近期";
    const range = feed.minPerModule && feed.maxPerModule ? `每模块 ${feed.minPerModule}-${feed.maxPerModule} 篇` : `${count} 篇`;
    const topPeriod = feed.topJournal && feed.topJournal.period ? `顶刊 ${feed.topJournal.period}` : "";
    $("#feedMeta").textContent = [updated, days, range, topPeriod].filter(Boolean).join(" · ");
  }

  function flattenPapersFromModules(modules) {
    return (modules || []).flatMap((module) => module.papers || []);
  }

  function entryPapers(entry) {
    if (!entry) return [];
    if (entry.papers) return entry.papers;
    return flattenPapersFromModules(entry.modules);
  }

  function topJournalEntries() {
    const top = feed.topJournal || {};
    const entries = [];
    if ((top.papers || []).length) {
      entries.push({
        date: top.period || top.updatedAt,
        label: `${top.period || "本月"} 顶刊推荐`,
        description: top.updatedAt ? `更新于 ${formatDate(top.updatedAt)}` : "本月顶刊相关论文",
        papers: top.papers || [],
        current: true,
      });
    }
    (top.archive || []).forEach((entry) => entries.push(entry));
    return entries;
  }

  function modulesForFeed() {
    const researchModules = feed.modules && feed.modules.length
      ? feed.modules.map((module) => ({ ...module, type: module.type || "daily" }))
      : [{ type: "daily", name: "今日推荐", papers: feed.papers || [] }];

    const dailyArchive = {
      type: "daily-archive",
      name: "每日论文归档",
      description: "前一日及更早的每日论文推荐会按日期自动收纳在这里。",
      entries: feed.dailyArchive || [],
    };

    const topJournal = feed.topJournal || {};
    const topJournalModule = {
      type: "top-journal",
      name: "顶刊相关论文",
      description: "每月检索 Nature、Science、PRL 等顶级期刊中与研究方向相关的论文。",
      papers: topJournal.papers || [],
      entries: topJournalEntries(),
      period: topJournal.period,
    };

    return [...researchModules, dailyArchive, topJournalModule];
  }

  function modulePaperCount(module) {
    if (!module) return 0;
    if (module.papers) return module.papers.length;
    if (module.entries) return module.entries.reduce((sum, entry) => sum + entryPapers(entry).length, 0);
    return 0;
  }

  function moduleMeta(module) {
    if (module.type === "daily-archive") {
      const entries = module.entries || [];
      return [`${entries.length} 个日期`, `${modulePaperCount(module)} 篇`, "点击进入"];
    }
    if (module.type === "top-journal") {
      const historyCount = Math.max(0, (module.entries || []).length - ((module.papers || []).length ? 1 : 0));
      return [`本月 ${(module.papers || []).length} 篇`, `历史 ${historyCount} 期`, "点击进入"];
    }
    const papers = module.papers || [];
    const arxivCount = papers.filter((paper) => normalize(paper.source).includes("arxiv")).length;
    const journalCount = papers.length - arxivCount;
    return [`arXiv ${arxivCount}`, `期刊 ${journalCount}`, "点击进入"];
  }

  function renderModuleDirectory(modules) {
    const list = $("#paperList");
    const directory = create("div", "module-directory");

    modules.forEach((module, index) => {
      const area = (profile.researchAreas || []).find((item) => item.name === module.name) || {};
      const card = create("button", "module-card");
      card.type = "button";
      card.setAttribute("aria-label", `进入${module.name || "研究模块"}`);

      const top = create("div", "module-card-top");
      top.appendChild(create("span", "module-number", String(index + 1).padStart(2, "0")));
      top.appendChild(create("span", "module-count", `${modulePaperCount(module)} 篇`));
      card.appendChild(top);

      card.appendChild(create("h3", "", module.name || "研究模块"));
      const description = module.description || area.description;
      if (description) card.appendChild(create("p", "", description));

      const meta = create("div", "module-card-meta");
      moduleMeta(module).forEach((item) => meta.appendChild(create("span", "", item)));
      card.appendChild(meta);

      card.addEventListener("click", () => {
        state.selectedModuleIndex = index;
        state.selectedEntryIndex = null;
        resetFilters();
        renderPapers();
        $("#papers").scrollIntoView({ behavior: "smooth", block: "start" });
      });
      directory.appendChild(card);
    });

    list.appendChild(directory);
  }

  function createBackButton(label, handler) {
    const back = create("button", "back-button", label);
    back.type = "button";
    back.addEventListener("click", handler);
    return back;
  }

  function renderEntryDirectory(module) {
    const list = $("#paperList");
    const group = create("section", "paper-module");
    const heading = create("div", "paper-module-heading");
    const titleWrap = create("div", "");

    titleWrap.appendChild(createBackButton("返回目录", () => {
      state.selectedModuleIndex = null;
      state.selectedEntryIndex = null;
      renderPapers();
    }));
    titleWrap.appendChild(create("h3", "", module.name || "归档目录"));
    heading.appendChild(titleWrap);
    heading.appendChild(create("span", "", `${(module.entries || []).length} 个目录`));
    group.appendChild(heading);

    const directory = create("div", "module-directory");
    (module.entries || []).forEach((entry, index) => {
      const papers = entryPapers(entry);
      const card = create("button", "module-card");
      card.type = "button";
      card.setAttribute("aria-label", `进入${entry.label || entry.date || "日期目录"}`);

      const top = create("div", "module-card-top");
      top.appendChild(create("span", "module-number", String(index + 1).padStart(2, "0")));
      top.appendChild(create("span", "module-count", `${papers.length} 篇`));
      card.appendChild(top);

      card.appendChild(create("h3", "", entry.label || formatDate(entry.date)));
      if (entry.description) card.appendChild(create("p", "", entry.description));

      const meta = create("div", "module-card-meta");
      meta.appendChild(create("span", "", formatDate(entry.date)));
      meta.appendChild(create("span", "", `${papers.length} 篇`));
      meta.appendChild(create("span", "", "点击进入"));
      card.appendChild(meta);

      card.addEventListener("click", () => {
        state.selectedEntryIndex = index;
        resetFilters();
        renderPapers();
      });
      directory.appendChild(card);
    });

    if (!module.entries || module.entries.length === 0) {
      group.appendChild(create("p", "empty-state-inline", "暂无历史目录。下一次自动更新后会开始归档。"));
    } else {
      group.appendChild(directory);
    }
    list.appendChild(group);
  }

  function paperMatches(paper) {
    const sourceMatch = state.source === "all" || normalize(paper.source).includes(normalize(state.source));
    if (!sourceMatch) return false;
    const haystack = normalize([
      paper.title,
      (paper.authors || []).join(" "),
      paper.abstract,
      paper.articleSummaryZh,
      paper.discussionFocusZh,
      paper.venue,
      paper.query,
      (paper.keywords || []).join(" "),
    ].join(" "));
    return !state.search || haystack.includes(normalize(state.search));
  }

  function createPaperCard(paper) {
    const card = create("article", "paper-card");

    const topline = create("div", "paper-topline");
    const sourceText = paper.source || "Journal";
    const source = create("span", `source-pill ${normalize(sourceText).includes("arxiv") ? "arxiv" : ""}`, sourceText);
    topline.appendChild(source);
    topline.appendChild(create("span", "", formatDate(paper.published)));
    if (paper.venue) topline.appendChild(create("span", "", paper.venue));
    if (paper.query) topline.appendChild(create("span", "", paper.query));
    card.appendChild(topline);

    card.appendChild(create("h3", "paper-title", paper.title || "Untitled"));
    if (paper.authors && paper.authors.length) {
      card.appendChild(create("p", "paper-authors", paper.authors.slice(0, 6).join(", ")));
    }

    const insightList = create("div", "paper-insights");
    [
      ["中文摘要", paper.abstractZh || paper.articleSummaryZh || paper.articleSummary || paper.abstract],
      ["讨论重点", paper.discussionFocusZh || paper.discussionFocus],
    ].filter((item) => item[1]).forEach(([label, value]) => {
      const item = create("p", "paper-insight");
      item.appendChild(create("strong", "", `${label}：`));
      item.appendChild(document.createTextNode(value));
      insightList.appendChild(item);
    });
    if (insightList.children.length) card.appendChild(insightList);

    if (paper.matchReasons && paper.matchReasons.length) {
      card.appendChild(create("p", "paper-reason", `匹配原因：${paper.matchReasons.join("；")}`));
    }

    const link = create("a", "paper-link", "打开论文");
    link.href = paper.url || "#";
    link.target = "_blank";
    link.rel = "noreferrer";
    card.appendChild(link);

    return card;
  }

  function selectedPaperSet(module) {
    if (!module) return [];
    if (module.entries && state.selectedEntryIndex === null) return null;
    if (module.entries && state.selectedEntryIndex !== null) {
      return entryPapers(module.entries[state.selectedEntryIndex]);
    }
    return module.papers || [];
  }

  function selectedTitle(module) {
    if (!module) return "研究模块";
    if (module.entries && state.selectedEntryIndex !== null) {
      const entry = module.entries[state.selectedEntryIndex];
      return entry ? entry.label || formatDate(entry.date) : module.name;
    }
    return module.name || "研究模块";
  }

  function renderPaperList(module) {
    const list = $("#paperList");
    const empty = $("#emptyState");
    const rawPapers = selectedPaperSet(module) || [];
    const papers = rawPapers.filter(paperMatches);

    const group = create("section", "paper-module");
    const heading = create("div", "paper-module-heading");
    const titleWrap = create("div", "");

    titleWrap.appendChild(createBackButton(module.entries ? "返回日期目录" : "返回目录", () => {
      if (module.entries && state.selectedEntryIndex !== null) {
        state.selectedEntryIndex = null;
      } else {
        state.selectedModuleIndex = null;
      }
      renderPapers();
    }));
    titleWrap.appendChild(create("h3", "", selectedTitle(module)));
    heading.appendChild(titleWrap);
    heading.appendChild(create("span", "", `${papers.length} 篇`));
    group.appendChild(heading);

    const cards = create("div", "paper-module-grid");
    papers.forEach((paper) => cards.appendChild(createPaperCard(paper)));
    group.appendChild(cards);
    list.appendChild(group);

    empty.hidden = papers.length > 0;
  }

  function renderPapers() {
    const list = $("#paperList");
    const empty = $("#emptyState");
    const controls = $(".paper-controls");
    const modules = modulesForFeed();
    const selectedModule = state.selectedModuleIndex === null ? null : modules[state.selectedModuleIndex];
    const browsingDirectory = !selectedModule || (selectedModule.entries && state.selectedEntryIndex === null);

    list.innerHTML = "";
    if (controls) controls.hidden = browsingDirectory;

    if (!selectedModule) {
      renderModuleDirectory(modules);
      empty.hidden = modules.some((module) => modulePaperCount(module) > 0 || (module.entries || []).length > 0);
      return;
    }

    if (selectedModule.entries && state.selectedEntryIndex === null) {
      renderEntryDirectory(selectedModule);
      empty.hidden = true;
      return;
    }

    renderPaperList(selectedModule);
  }

  function bindControls() {
    const search = $("#paperSearch");
    search.addEventListener("input", (event) => {
      state.search = event.target.value.trim();
      renderPapers();
    });

    document.querySelectorAll(".filter-button").forEach((button) => {
      button.addEventListener("click", () => {
        document.querySelectorAll(".filter-button").forEach((item) => item.classList.remove("active"));
        button.classList.add("active");
        state.source = button.dataset.source;
        renderPapers();
      });
    });
  }

  renderProfile();
  renderFeedMeta();
  renderPapers();
  bindControls();
})();
