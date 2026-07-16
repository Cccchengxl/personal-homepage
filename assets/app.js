(function () {
  const profile = window.SITE_PROFILE || {};
  const feed = window.RESEARCH_PAPER_FEED || { papers: [] };
  const state = { source: "all", search: "", selectedModuleIndex: null };

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

  const formatDate = (value) => {
    if (!value) return "日期待定";
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return value;
    return date.toLocaleDateString("zh-CN", { year: "numeric", month: "short", day: "numeric" });
  };

  const normalize = (value) => String(value || "").toLowerCase();

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
    $("#feedMeta").textContent = `${updated} · ${days} · ${range}`;
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
      paper.mainConclusionZh,
      paper.venue,
      paper.query,
      (paper.keywords || []).join(" "),
    ].join(" "));
    return !state.search || haystack.includes(normalize(state.search));
  }

  function modulesForFeed() {
    return feed.modules && feed.modules.length
      ? feed.modules
      : [{ name: "今日推荐", papers: feed.papers || [] }];
  }

  function renderModuleDirectory(modules) {
    const list = $("#paperList");
    const directory = create("div", "module-directory");

    modules.forEach((module, index) => {
      const papers = module.papers || [];
      const area = (profile.researchAreas || []).find((item) => item.name === module.name) || {};
      const card = create("button", "module-card");
      card.type = "button";
      card.setAttribute("aria-label", `进入${module.name || "研究模块"}`);

      const top = create("div", "module-card-top");
      top.appendChild(create("span", "module-number", String(index + 1).padStart(2, "0")));
      top.appendChild(create("span", "module-count", `${papers.length} 篇`));
      card.appendChild(top);

      card.appendChild(create("h3", "", module.name || "研究模块"));
      if (area.description) card.appendChild(create("p", "", area.description));

      const meta = create("div", "module-card-meta");
      const arxivCount = papers.filter((paper) => normalize(paper.source).includes("arxiv")).length;
      const journalCount = papers.length - arxivCount;
      meta.appendChild(create("span", "", `arXiv ${arxivCount}`));
      meta.appendChild(create("span", "", `期刊 ${journalCount}`));
      meta.appendChild(create("span", "", "点击进入"));
      card.appendChild(meta);

      card.addEventListener("click", () => {
        state.selectedModuleIndex = index;
        state.search = "";
        state.source = "all";
        const search = $("#paperSearch");
        if (search) search.value = "";
        document.querySelectorAll(".filter-button").forEach((item) => {
          item.classList.toggle("active", item.dataset.source === "all");
        });
        renderPapers();
        $("#papers").scrollIntoView({ behavior: "smooth", block: "start" });
      });
      directory.appendChild(card);
    });

    list.appendChild(directory);
  }

  function createPaperCard(paper) {
    const card = create("article", "paper-card");

    const topline = create("div", "paper-topline");
    const source = create("span", `source-pill ${normalize(paper.source).includes("arxiv") ? "arxiv" : ""}`, paper.source || "Journal");
    topline.appendChild(source);
    topline.appendChild(create("span", "", formatDate(paper.published)));
    if (paper.venue) topline.appendChild(create("span", "", paper.venue));
    card.appendChild(topline);

    card.appendChild(create("h3", "paper-title", paper.title || "Untitled"));
    if (paper.authors && paper.authors.length) {
      card.appendChild(create("p", "paper-authors", paper.authors.slice(0, 6).join(", ")));
    }
    const insightList = create("div", "paper-insights");
    [
      ["文章摘要", paper.articleSummaryZh || paper.articleSummary || paper.abstract],
      ["讨论重点", paper.discussionFocusZh || paper.discussionFocus],
      ["主要结论", paper.mainConclusionZh || paper.mainConclusion],
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

  function renderPapers() {
    const list = $("#paperList");
    const empty = $("#emptyState");
    list.innerHTML = "";

    const modules = modulesForFeed();
    const controls = $(".paper-controls");
    if (controls) controls.hidden = state.selectedModuleIndex === null;

    if (state.selectedModuleIndex === null) {
      renderModuleDirectory(modules);
      empty.hidden = modules.some((module) => (module.papers || []).length > 0);
      return;
    }

    const selectedModule = modules[state.selectedModuleIndex] || modules[0];
    if (!selectedModule) {
      empty.hidden = false;
      return;
    }

    let visibleCount = 0;

    const papers = (selectedModule.papers || []).filter(paperMatches);
    visibleCount = papers.length;

    const group = create("section", "paper-module");
    const heading = create("div", "paper-module-heading");
    const titleWrap = create("div", "");
    const back = create("button", "back-button", "返回目录");
    back.type = "button";
    back.addEventListener("click", () => {
      state.selectedModuleIndex = null;
      renderPapers();
    });
    titleWrap.appendChild(back);
    titleWrap.appendChild(create("h3", "", selectedModule.name || "研究模块"));
    heading.appendChild(titleWrap);
    heading.appendChild(create("span", "", `${papers.length} 篇`));
    group.appendChild(heading);

    const cards = create("div", "paper-module-grid");
    papers.forEach((paper) => cards.appendChild(createPaperCard(paper)));
    group.appendChild(cards);
    list.appendChild(group);

    empty.hidden = visibleCount > 0;
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
