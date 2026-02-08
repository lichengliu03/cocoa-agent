# 📊 Fed Rate Cut Stock Inflection - CocoaBench任务

## 概述

这是一个完整的CocoaBench任务示例，展示如何使用Vercel托管交互式界面。

**任务目标：** 分析2024年9月18日美联储降息事件对三只科技股的影响，判断有多少只股票出现了价格拐点。

## 🎯 任务特点

- ✅ **GUI + 编程结合** - 从网页提取数据 + Python统计分析
- ✅ **多步骤解决** - 需要5-10分钟完成
- ✅ **确定性答案** - 答案是整数（0-3）
- ✅ **有挑战性** - 需要理解金融概念和统计方法
- ✅ **使用Vercel** - 易于部署和维护

## 📁 文件清单

### Web界面文件（部署到Vercel）
- `index.html` - 交互式股票图表界面
- `vercel.json` - Vercel配置
- `deploy.sh` - 自动部署脚本

### CocoaBench任务文件
- `instruction.md` - 任务指令（给AI agent）
- `evaluation.md` - 评估标准和答案
- `solution.md` - 人类解决方案步骤
- `metadata.json` - 任务元数据

### 文档
- `README.md` - 项目说明
- `DEPLOYMENT_GUIDE.md` - 详细部署指南
- `SUMMARY.md` - 本文件

## 🚀 快速开始

### 1. 部署到Vercel

```bash
cd /u/lliu22/cocoa-agent/vercel-stock-example

# 方法A：使用自动脚本
./deploy.sh

# 方法B：手动部署
vercel --prod
```

### 2. 测试界面

访问部署后的URL，确保：
- 三个股票图表正常显示
- "Show Price Data"按钮可以展开数据表
- 数据完整且正确

### 3. 移动到CocoaBench

```bash
# 创建任务目录
mkdir -p ../cocoabench-head/fed-rate-cut-stock-inflection

# 复制任务文件
cp instruction.md evaluation.md solution.md metadata.json \
   ../cocoabench-head/fed-rate-cut-stock-inflection/
```

### 4. 测试任务

用至少一个AI agent测试任务：
- 推荐：Claude 4.5, GPT-4, Gemini 3 Pro
- 记录结果和聊天记录链接
- 更新evaluation.md中的测试结果

### 5. 加密并提交

```bash
cd ../contrib

# 加密
python encrypt_tasks.py --task fed-rate-cut-stock-inflection

# 验证
python validate_task.py fed-rate-cut-stock-inflection --check-encrypted

# 提交PR
git checkout -b task/fed-rate-cut-stock-inflection
git add ../cocoabench-head/fed-rate-cut-stock-inflection/
git commit -m "Add task: fed-rate-cut-stock-inflection"
git push origin task/fed-rate-cut-stock-inflection
```

## 📊 数据说明

### 股票映射（仅供参考，不在任务中透露）
- **Stock A** = NVIDIA (NVDA)
- **Stock B** = Microsoft (MSFT)
- **Stock C** = AMD

### 时间范围
- 2024年9月6日 - 9月27日（16个交易日）
- 关键日期：9月18日（美联储降息）
- 分析窗口：9月16-20日（±2交易日）

### 正确答案
**2** - NVIDIA和AMD在降息前后出现价格拐点

## 🔧 自定义选项

### 增加难度
1. 隐藏部分数据，需要多次点击
2. 添加更多干扰股票
3. 使用不同的日期格式
4. 要求更复杂的统计分析

### 降低难度
1. 提供JSON API端点
2. 在界面上显示计算提示
3. 减少需要分析的股票数量

### 修改数据
编辑`index.html`中的`stockData`对象：

```javascript
const stockData = {
    A: {
        dates: ['2024-09-06', ...],
        prices: [102.83, ...]
    },
    // ...
};
```

## 🎓 学习价值

这个任务教会AI agent：
1. **Web交互** - 导航网页、点击按钮、提取数据
2. **数据处理** - 解析表格、转换格式
3. **金融计算** - 对数收益率、移动统计
4. **条件判断** - 复杂的逻辑条件
5. **代码编写** - Python数据分析

## 📝 注意事项

1. **URL更新** - 部署后记得更新instruction.md和evaluation.md中的URL
2. **数据验证** - 确保股票数据准确无误
3. **答案验证** - 自己先手动计算一遍确认答案
4. **Agent测试** - 至少测试一个agent并记录结果
5. **加密必须** - 提交PR前必须加密任务文件

## 🤝 贡献

如果你基于这个模板创建了新任务：
1. 修改股票数据和分析条件
2. 更新任务名称和元数据
3. 重新计算正确答案
4. 测试并提交PR

## 📞 支持

- CocoaBench文档: https://cocoabench.github.io/
- 贡献指南: `/u/lliu22/cocoa-agent/contrib/CONTRIBUTING.md`
- GitHub Issues: https://github.com/cocoabench/cocoa-agent/issues

---

**创建日期:** 2026-02-07
**任务类型:** GUI + Coding
**难度:** Medium
**预计时间:** 10-15分钟
