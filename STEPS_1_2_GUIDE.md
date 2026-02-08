# 📋 第一步和第二步完成指南

## 当前状态

✅ **已完成：**
- Web界面文件已准备好（`/u/lliu22/cocoa-agent/vercel-stock-example/`）
- 任务文件已添加到benchmark（`/u/lliu22/cocoa-agent/cocoabench-head/fed-rate-cut-stock-inflection/`）
- URL更新脚本已创建（`update_urls.sh`）
- 本地测试服务器已验证工作正常

⚠️ **需要手动完成：**
- 部署到Vercel（系统缺少Node.js/npm）
- 更新任务文件中的URL

---

## 🚀 第一步：部署到Vercel

### 方法A：通过Vercel Web界面（最简单）

1. **访问** https://vercel.com 并登录

2. **点击** "Add New..." → "Project"

3. **选择部署方式：**

   **选项1：从GitHub导入（推荐）**
   ```bash
   # 先推送到GitHub
   cd /u/lliu22/cocoa-agent
   git add vercel-stock-example/
   git commit -m "Add stock analysis web interface"
   git push
   ```
   然后在Vercel中导入该仓库，Root Directory设置为 `vercel-stock-example`

   **选项2：直接拖拽文件**
   - 将 `vercel-stock-example` 文件夹拖到Vercel界面
   - 或者只上传 `index.html` 和 `vercel.json`

4. **配置项目：**
   - Framework Preset: Other
   - Root Directory: `vercel-stock-example` (如果从仓库导入)
   - Build Command: 留空
   - Output Directory: 留空

5. **部署并获取URL**
   - 点击 "Deploy"
   - 等待1-2分钟
   - 复制生成的URL（例如：`https://stock-analysis-abc123.vercel.app`）

### 方法B：本地测试（临时方案）

如果暂时无法部署到Vercel，可以先用本地服务器测试：

```bash
cd /u/lliu22/cocoa-agent/vercel-stock-example
python3 -m http.server 8888
```

然后访问 `http://localhost:8888`

---

## 🔄 第二步：更新URL

### 自动更新（推荐）

获得Vercel URL后，运行：

```bash
cd /u/lliu22/cocoa-agent/vercel-stock-example
./update_urls.sh https://your-actual-url.vercel.app
```

这会自动更新以下文件中的所有URL：
- `cocoabench-head/fed-rate-cut-stock-inflection/task.yaml`
- `cocoabench-head/fed-rate-cut-stock-inflection/instruction.md`
- `cocoabench-head/fed-rate-cut-stock-inflection/evaluation.md`

### 手动更新

如果需要手动更新，替换这些文件中的 `https://your-app.vercel.app`：

1. **task.yaml** (第7行)
2. **instruction.md** (第5行)
3. **evaluation.md** (第5行)

---

## ✅ 验证部署

部署成功后，访问你的URL应该看到：

- ✅ 页面标题："Stock Analysis Dashboard"
- ✅ 三个股票图表（Stock A, B, C）
- ✅ 每个图表下方有 "Show Price Data" 按钮
- ✅ 点击按钮展开价格数据表格
- ✅ 红色虚线标注2024年9月18日

---

## 📝 完成后的检查清单

- [ ] Web界面已部署到Vercel
- [ ] 获得了Vercel URL
- [ ] 运行了 `update_urls.sh` 脚本
- [ ] 验证了三个任务文件中的URL已更新
- [ ] 访问Vercel URL确认界面正常工作

---

## 🎯 下一步

完成第一步和第二步后，你可以继续：

**第三步：测试任务**
```bash
cd /u/lliu22/cocoa-agent
python inference_main.py \
  --config configs/my-config.json \
  --tasks-dir cocoabench-head/ \
  --task-name fed-rate-cut-stock-inflection \
  --output-dir results/
```

**第四步：用AI Agent测试**
- 推荐：Claude 4.5, GPT-4, Gemini 3 Pro
- 记录结果并更新 `evaluation.md`

**第五步：加密任务**
```bash
cd /u/lliu22/cocoa-agent/contrib
python encrypt_tasks.py --task fed-rate-cut-stock-inflection
```

**第六步：提交PR**
```bash
git checkout -b task/fed-rate-cut-stock-inflection
git add cocoabench-head/fed-rate-cut-stock-inflection/
git commit -m "Add task: fed-rate-cut-stock-inflection"
git push origin task/fed-rate-cut-stock-inflection
```

---

## 🆘 需要帮助？

如果你遇到问题或获得了Vercel URL，请告诉我：
- 我可以帮你运行URL更新脚本
- 我可以验证更新是否成功
- 我可以帮你测试任务

**准备好后，请告诉我你的Vercel URL！** 🚀
