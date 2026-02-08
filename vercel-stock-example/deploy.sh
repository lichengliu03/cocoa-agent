#!/bin/bash

# CocoaBench任务部署脚本
# 用于快速部署股票分析任务到Vercel

set -e

echo "🚀 CocoaBench Stock Analysis Task - Vercel Deployment"
echo "=================================================="
echo ""

# 检查是否安装了vercel CLI
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI未安装"
    echo "请运行: npm install -g vercel"
    exit 1
fi

echo "✅ Vercel CLI已安装"
echo ""

# 检查是否已登录
echo "📝 检查Vercel登录状态..."
if ! vercel whoami &> /dev/null; then
    echo "请先登录Vercel:"
    vercel login
fi

echo "✅ 已登录Vercel"
echo ""

# 部署到Vercel
echo "🚀 开始部署到Vercel..."
DEPLOY_OUTPUT=$(vercel --prod --yes)
echo "$DEPLOY_OUTPUT"

# 提取部署URL
DEPLOY_URL=$(echo "$DEPLOY_OUTPUT" | grep -oP 'https://[^\s]+' | tail -1)

if [ -z "$DEPLOY_URL" ]; then
    echo "❌ 无法获取部署URL"
    exit 1
fi

echo ""
echo "✅ 部署成功！"
echo "📍 URL: $DEPLOY_URL"
echo ""

# 更新instruction.md和evaluation.md中的URL
echo "📝 更新任务文件中的URL..."

sed -i "s|https://your-app.vercel.app|$DEPLOY_URL|g" instruction.md
sed -i "s|https://your-app.vercel.app|$DEPLOY_URL|g" evaluation.md

echo "✅ 任务文件已更新"
echo ""

# 显示下一步操作
echo "🎯 下一步操作:"
echo "1. 访问 $DEPLOY_URL 测试界面"
echo "2. 将任务文件移动到 cocoabench-head/:"
echo "   mkdir -p ../cocoabench-head/fed-rate-cut-stock-inflection"
echo "   cp instruction.md evaluation.md solution.md metadata.json ../cocoabench-head/fed-rate-cut-stock-inflection/"
echo ""
echo "3. 用AI agent测试任务并更新evaluation.md"
echo ""
echo "4. 加密任务:"
echo "   cd ../contrib"
echo "   python encrypt_tasks.py --task fed-rate-cut-stock-inflection"
echo ""
echo "5. 验证并提交PR"
echo ""
echo "✨ 完成！"
