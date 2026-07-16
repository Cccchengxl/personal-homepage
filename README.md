# 个人学术主页

这是一个可直接打开的静态个人主页模板，包含个人介绍、研究方向、代表性成果和每日论文推荐模块。

## 本地预览

直接打开 `index.html` 即可预览页面。页面读取的是 `data/profile.js` 和 `data/papers.js`，所以不依赖本地服务器。

## 当前论文推荐模块

每天北京时间 08:00 推荐两组论文，每组目标 5 到 10 篇：

- 机器学习分子动力学模拟与热力学性质：机器学习势函数、分子动力学模拟、DeepMD、DeePMD-kit、MACE、自由能、热输运、相变和热力学性质。
- 凝聚态物理强关联体系和多铁性质：强关联电子、Hubbard 模型、Mott 绝缘体、非常规超导、量子自旋液体、重费米子、DMFT、DMRG、张量网络、多铁材料和磁电耦合。

论文推荐区采用目录样式：先显示两个研究模块，点击模块后进入对应论文列表。每篇推荐论文会显示三项中文信息：文章摘要、讨论重点和主要结论。

## 修改个人信息和研究方向

编辑 `data/profile.json`：

- `name`、`title`、`affiliation`、`email`：个人基本信息。
- `links`：主页底部链接，已包含 Google Scholar。
- `researchAreas`：主页展示的两个研究模块。
- `paperFeed.queries`：每日论文抓取关键词和 arXiv 分类。
- `paperFeed.minPerModule`、`paperFeed.maxPerModule`：每个模块的推荐篇数范围。
- `publications`：代表性论文或项目。

修改后运行：

```bash
python scripts/fetch_papers.py --config data/profile.json
```

脚本会同步生成：

- `data/profile.js`
- `data/papers.json`
- `data/papers.js`
- `data/latest-papers.md`

## 每日论文来源

默认抓取两类内容：

- arXiv：预印本论文，按 `paperFeed.queries[].keywords` 和 `arxivCategories` 检索。
- Crossref：近期带 DOI 的期刊文章元数据，类型限定为 `journal-article`。

注意：Crossref 能代表“已发表期刊论文元数据”，但不能保证论文属于 SCI。严格 SCI 检索通常需要 Clarivate Web of Science API、机构订阅，或者维护一份目标 SCI 期刊白名单。

## GitHub Pages 自动更新

把本目录作为 GitHub 仓库发布到 GitHub Pages 后，`.github/workflows/daily-papers.yml` 会每天北京时间 08:00 运行一次并提交最新论文数据。

如需邮件推送，在仓库 Secrets 中配置：

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USER`
- `SMTP_PASSWORD`
- `MAIL_FROM`
- `MAIL_TO`
- `SMTP_STARTTLS`，可选，默认启用

如果不配置 SMTP，网页仍会每天更新，邮件步骤会自动跳过。
