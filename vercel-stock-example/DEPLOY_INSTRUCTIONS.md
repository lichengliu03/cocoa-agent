# 🚀 Vercel部署说明

## 当前状态

系统上未安装Node.js/npm，无法使用Vercel CLI。但我已经为你准备好了所有部署文件。

## 方法1：通过Vercel Web界面部署（推荐）

### 步骤：

1. **访问Vercel**
   - 打开 https://vercel.com
   - 使用GitHub账号登录

2. **创建新项目**
   - 点击 "Add New..." → "Project"
   - 选择 "Import Git Repository"

3. **导入仓库**

   **选项A：如果已经推送到GitHub**
   - 选择包含 `vercel-stock-example` 的仓库
   - Root Directory 设置为 `vercel-stock-example`

   **选项B：如果还没推送到GitHub**
   - 先在本地执行：
     ```bash
     cd /u/lliu22/cocoa-agent
     git add vercel-stock-example/
     git commit -m "Add stock analysis web interface"
     git push
     ```
   - 然后在Vercel中导入仓库

4. **配置项目**
   - Framework Preset: 选择 "Other"
   - Root Directory: `vercel-stock-example`
   - Build Command: 留空
   - Output Directory: 留空
   - Install Command: 留空

5. **部署**
   - 点击 "Deploy"
   - 等待部署完成（通常1-2分钟）

6. **获取URL**
   - 部署成功后，你会看到类似这样的URL：
     `https://vercel-stock-example-abc123.vercel.app`
   - 复制这个URL

## 方法2：使用Vercel CLI（需要在有Node.js的机器上）

如果你有另一台安装了Node.js的机器：

```bash
# 安装Vercel CLI
npm install -g vercel

# 登录
vercel login

# 进入目录
cd /u/lliu22/cocoa-agent/vercel-stock-example

# 部署
vercel --prod
```

## 方法3：直接上传文件

1. 访问 https://vercel.com/new
2. 选择 "Deploy from template" 或 "Import project"
3. 上传 `index.html` 和 `vercel.json` 文件
4. 点击部署

## 部署后的操作

部署成功后，你会得到一个URL，例如：
```
https://stock-analysis-xyz123.vercel.app
```

**请将这个URL告诉我，我会帮你更新任务文件中的所有URL占位符。**

或者你可以手动更新以下文件：
1. `/u/lliu22/cocoa-agent/cocoabench-head/fed-rate-cut-stock-inflection/task.yaml`
2. `/u/lliu22/cocoa-agent/cocoabench-head/fed-rate-cut-stock-inflection/instruction.md`
3. `/u/lliu22/cocoa-agent/cocoabench-head/fed-rate-cut-stock-inflection/evaluation.md`

将所有 `https://your-app.vercel.app` 替换为你的实际URL。

## 需要部署的文件

已准备好的文件位于：`/u/lliu22/cocoa-agent/vercel-stock-example/`

- ✅ index.html - 交互式股票图表
- ✅ vercel.json - Vercel配置
- ✅ README.md - 说明文档

## 测试部署

部署成功后，访问你的URL，应该能看到：
- 三个股票图表（Stock A, B, C）
- 每个图表下方有 "Show Price Data" 按钮
- 点击按钮可以展开价格数据表格
- 红色虚线标注了2024年9月18日（美联储降息日）

## 遇到问题？

- 确保 `index.html` 和 `vercel.json` 在同一目录
- 检查Vercel项目设置中的Root Directory
- 查看Vercel部署日志了解错误信息

---

**准备好后，请告诉我你的Vercel URL，我会立即更新任务文件！** 🚀
