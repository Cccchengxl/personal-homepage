# 公开发布方式

当前站点是纯静态网页，可以部署到任何静态托管服务。

## 最快方式：Netlify Drop

1. 打开 https://app.netlify.com/drop
2. 上传 `personal-homepage-public.zip`，或把 `personal-homepage` 文件夹拖进去。
3. Netlify 会生成一个别人可以访问的公开网址。

## GitHub Pages

1. 新建一个 GitHub 仓库。
2. 上传本目录中的所有文件。
3. 在仓库设置中启用 Pages，来源选择仓库根目录。
4. `.github/workflows/daily-papers.yml` 会每天北京时间 08:00 更新论文数据。

## Vercel

1. 新建 Vercel 项目。
2. 选择本目录作为静态项目。
3. 不需要构建命令，输出目录为项目根目录。

## 注意

公开发布后，页面中的邮箱、Google Scholar 链接和论文推荐内容会被任何访问者看到。
