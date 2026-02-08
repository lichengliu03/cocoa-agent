# Stock Analysis Dashboard - Vercel Deployment

这是一个用于CocoaBench任务的交互式股票分析界面示例。

## 功能特点

- 📊 显示三只匿名股票的价格走势图
- 🔍 需要点击按钮才能查看具体价格数据
- 📅 标注了美联储降息日期（2024年9月18日）
- 💻 Agent需要提取数据并编写代码进行分析

## 部署到Vercel

### 方法1：通过Vercel CLI

```bash
# 安装Vercel CLI
npm i -g vercel

# 登录
vercel login

# 部署
cd vercel-stock-example
vercel --prod
```

### 方法2：通过GitHub + Vercel Dashboard

1. 将这个文件夹推送到GitHub仓库
2. 在 https://vercel.com 登录
3. 点击 "New Project"
4. 导入你的GitHub仓库
5. Vercel会自动检测并部署

## 本地测试

```bash
# 使用Python简单HTTP服务器
python -m http.server 8080

# 或使用Node.js
npx serve
```

然后访问 http://localhost:8080

## 数据说明

- **Stock A** = NVIDIA (NVDA)
- **Stock B** = Microsoft (MSFT)
- **Stock C** = AMD

数据时间范围：2024年9月6日 - 9月27日

## 在CocoaBench任务中使用

在 `instruction.md` 中引用部署后的URL：

```markdown
Visit the stock analysis dashboard at https://your-app.vercel.app
```

在 `evaluation.md` 中设置：

```markdown
## Initialization

Host UI: https://your-app.vercel.app
```
