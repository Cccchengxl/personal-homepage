# GitHub Pages 自动更新部署说明

目标：把这个目录上传到 GitHub 后，网页会公开访问，并且每天北京时间 08:00 自动更新论文推荐。

## 1. 新建仓库

1. 登录 GitHub 账号 `Cccchengxl`。
2. 打开 https://github.com/new
3. Repository name 建议填：`personal-homepage`
4. Visibility 建议选 `Public`。
5. 不要勾选初始化 README、.gitignore 或 license，因为本目录已经准备好了文件。
6. 点击 `Create repository`。

## 2. 上传文件

在新仓库页面：

1. 点击 `uploading an existing file`。
2. 打开本地目录 `outputs/personal-homepage`。
3. 把里面的所有文件和文件夹都拖到 GitHub 上传区。
4. 必须包含这些项目：
   - `.github/workflows/daily-papers.yml`
   - `index.html`
   - `assets/`
   - `data/`
   - `scripts/`
   - `.nojekyll`
5. Commit message 可以写：`Initial personal homepage`
6. 点击 `Commit changes`。

如果 GitHub 网页上传时没有带上隐藏文件夹 `.github`，需要手动新建文件：

1. 点击 `Add file` -> `Create new file`。
2. 文件名输入：`.github/workflows/daily-papers.yml`
3. 把本地同名文件内容复制进去并提交。

## 3. 开启 GitHub Pages

1. 进入仓库 `Settings`。
2. 左侧点击 `Pages`。
3. Build and deployment 的 Source 选择 `GitHub Actions`。
4. 保存。

## 4. 首次手动运行

1. 进入仓库 `Actions`。
2. 如果 GitHub 提示启用 workflows，点击允许。
3. 选择 `Daily paper refresh and Pages deploy`。
4. 点击 `Run workflow`。
5. 等待绿色对勾完成。

完成后，仓库的 `Settings` -> `Pages` 会显示公开网址，通常类似：

`https://cccchengxl.github.io/personal-homepage/`

## 5. 后续自动更新

`.github/workflows/daily-papers.yml` 会每天北京时间 08:00 自动运行：

1. 抓取 arXiv 和 Crossref 论文。
2. 更新 `data/papers.json`、`data/papers.js` 和 `data/latest-papers.md`。
3. 自动提交更新。
4. 自动部署 GitHub Pages。

你不需要每天重新上传 zip。

## 邮件推送可选

如果还想让 GitHub Actions 发邮件，需要在仓库 `Settings` -> `Secrets and variables` -> `Actions` 中添加 SMTP 配置：

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USER`
- `SMTP_PASSWORD`
- `MAIL_FROM`
- `MAIL_TO`
- `SMTP_STARTTLS`，可选

不配置邮件也没关系，网页仍会每天自动更新。
