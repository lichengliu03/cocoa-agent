# 使用Vercel部署CocoaBench任务 - 完整指南

## ✅ 为什么选择Vercel

1. **简单快速** - 一条命令即可部署
2. **免费托管** - 个人项目完全免费
3. **自动HTTPS** - 自动配置SSL证书
4. **全球CDN** - 快速访问
5. **已有先例** - CocoaBench的示例任务已在使用

## 📁 文件结构

```
vercel-stock-example/
├── index.html          # 交互式股票图表界面
├── vercel.json         # Vercel配置文件
├── README.md           # 部署说明
├── instruction.md      # CocoaBench任务指令
├── evaluation.md       # 评估标准和答案
├── solution.md         # 解决方案步骤
└── metadata.json       # 任务元数据
```

## 🚀 部署步骤

### 方法1：使用Vercel CLI（推荐）

```bash
# 1. 安装Vercel CLI
npm install -g vercel

# 2. 登录Vercel账号
vercel login

# 3. 进入项目目录
cd /u/lliu22/cocoa-agent/vercel-stock-example

# 4. 部署到生产环境
vercel --prod

# 5. 记录部署后的URL（例如：https://stock-analysis-abc123.vercel.app）
```

### 方法2：通过GitHub + Vercel Dashboard

```bash
# 1. 创建GitHub仓库并推送代码
git init
git add .
git commit -m "Add stock analysis task"
git remote add origin https://github.com/yourusername/stock-analysis.git
git push -u origin main

# 2. 访问 https://vercel.com
# 3. 点击 "New Project"
# 4. 导入你的GitHub仓库
# 5. Vercel会自动检测并部署
```

## 📝 部署后的配置

### 1. 更新任务文件中的URL

部署成功后，你会得到一个URL，例如：`https://stock-analysis-abc123.vercel.app`

需要在以下文件中更新这个URL：

**instruction.md:**
```markdown
Visit the stock analysis dashboard at https://stock-analysis-abc123.vercel.app
```

**evaluation.md:**
```markdown
## Initialization

Host UI: https://stock-analysis-abc123.vercel.app
```

### 2. 移动到CocoaBench任务目录

```bash
# 创建任务目录
mkdir -p /u/lliu22/cocoa-agent/cocoabench-head/fed-rate-cut-stock-inflection

# 复制任务文件（不包括index.html等web文件）
cp instruction.md evaluation.md solution.md metadata.json \
   /u/lliu22/cocoa-agent/cocoabench-head/fed-rate-cut-stock-inflection/
```

### 3. 加密任务（提交前必须）

```bash
cd /u/lliu22/cocoa-agent/contrib

# 加密任务
python encrypt_tasks.py --task fed-rate-cut-stock-inflection

# 验证加密
python validate_task.py fed-rate-cut-stock-inflection --check-encrypted
```

## 🧪 本地测试

在部署到Vercel之前，可以本地测试：

```bash
# 方法1：Python HTTP服务器
cd /u/lliu22/cocoa-agent/vercel-stock-example
python -m http.server 8080

# 方法2：使用npx serve
npx serve

# 访问 http://localhost:8080
```

## 🎯 任务特点

这个任务完美符合CocoaBench的要求：

- ✅ **GUI + 编程结合** - 需要从网页提取数据，然后编写代码分析
- ✅ **多步骤** - 数据提取 → 计算对数收益 → 统计分析 → 判断条件
- ✅ **确定性答案** - 答案是0-3之间的整数
- ✅ **有挑战性** - 需要理解金融概念和统计方法

## 💡 优化建议

### 增加难度的方式：

1. **隐藏部分数据** - 需要滚动或点击多次才能看到所有数据
2. **添加干扰信息** - 显示其他无关的股票指标
3. **数据格式变化** - 不同股票使用不同的日期格式
4. **需要多次交互** - 每次只显示5天的数据，需要翻页

### 降低难度的方式：

1. **提供API端点** - 允许直接下载JSON格式的数据
2. **显示提示** - 在界面上标注关键日期
3. **提供计算示例** - 在页面上显示一个样例计算

## 🔒 安全考虑

- Vercel上的数据是公开的，但通过匿名化（Stock A/B/C）增加了难度
- 真正的答案和映射关系只在加密的evaluation.md中
- 即使AI能访问网页，也需要正确的计算才能得到答案

## 📊 预期Agent表现

- **GPT-4** - 可能成功（擅长数据分析）
- **Claude 4.5** - 可能成功（擅长代码编写）
- **Gemini 3 Pro** - 可能失败（统计计算容易出错）

建议测试至少一个agent并记录结果！
