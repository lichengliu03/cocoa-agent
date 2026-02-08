# 🚀 快速参考

## 一键部署

```bash
cd /u/lliu22/cocoa-agent/vercel-stock-example
./deploy.sh
```

## 文件用途

| 文件 | 用途 | 部署到Vercel? |
|------|------|--------------|
| `index.html` | 交互式股票图表界面 | ✅ 是 |
| `vercel.json` | Vercel配置文件 | ✅ 是 |
| `instruction.md` | 任务指令（给AI agent） | ❌ 否 - 移到cocoabench-head |
| `evaluation.md` | 评估标准和答案 | ❌ 否 - 移到cocoabench-head |
| `solution.md` | 解决方案步骤 | ❌ 否 - 移到cocoabench-head |
| `metadata.json` | 任务元数据 | ❌ 否 - 移到cocoabench-head |
| `deploy.sh` | 自动部署脚本 | ❌ 否 - 仅本地使用 |

## 关键命令

```bash
# 部署
vercel --prod

# 本地测试
python -m http.server 8080

# 移动任务文件
mkdir -p ../cocoabench-head/fed-rate-cut-stock-inflection
cp instruction.md evaluation.md solution.md metadata.json \
   ../cocoabench-head/fed-rate-cut-stock-inflection/

# 加密任务
cd ../contrib
python encrypt_tasks.py --task fed-rate-cut-stock-inflection

# 验证
python validate_task.py fed-rate-cut-stock-inflection --check-encrypted
```

## 答案

**2** (NVIDIA和AMD)

## 下一步

1. ✅ 部署到Vercel
2. ✅ 更新URL
3. ⬜ 测试界面
4. ⬜ 用AI agent测试
5. ⬜ 移动文件到cocoabench-head
6. ⬜ 加密
7. ⬜ 提交PR

## 问题排查

**Q: 部署失败？**
- 检查是否安装了vercel CLI: `npm install -g vercel`
- 检查是否登录: `vercel whoami`

**Q: 图表不显示？**
- 检查浏览器控制台是否有错误
- 确认Chart.js CDN可访问

**Q: 数据不正确？**
- 检查index.html中的stockData对象
- 确认日期和价格匹配

**Q: Agent测试失败？**
- 这是好事！说明任务有挑战性
- 记录失败原因并更新evaluation.md
