#!/bin/bash

# URL更新脚本
# 用法: ./update_urls.sh <your-vercel-url>

if [ -z "$1" ]; then
    echo "❌ 错误: 请提供Vercel URL"
    echo "用法: ./update_urls.sh https://your-app.vercel.app"
    exit 1
fi

NEW_URL="$1"
OLD_URL="https://your-app.vercel.app"

echo "🔄 更新URL..."
echo "从: $OLD_URL"
echo "到: $NEW_URL"
echo ""

# 更新task.yaml
echo "📝 更新 task.yaml..."
sed -i "s|$OLD_URL|$NEW_URL|g" ../cocoabench-head/fed-rate-cut-stock-inflection/task.yaml

# 更新instruction.md
echo "📝 更新 instruction.md..."
sed -i "s|$OLD_URL|$NEW_URL|g" ../cocoabench-head/fed-rate-cut-stock-inflection/instruction.md

# 更新evaluation.md
echo "📝 更新 evaluation.md..."
sed -i "s|$OLD_URL|$NEW_URL|g" ../cocoabench-head/fed-rate-cut-stock-inflection/evaluation.md

echo ""
echo "✅ 完成！已更新以下文件："
echo "  - cocoabench-head/fed-rate-cut-stock-inflection/task.yaml"
echo "  - cocoabench-head/fed-rate-cut-stock-inflection/instruction.md"
echo "  - cocoabench-head/fed-rate-cut-stock-inflection/evaluation.md"
echo ""
echo "🔍 验证更新："
echo ""
echo "task.yaml:"
grep -n "$NEW_URL" ../cocoabench-head/fed-rate-cut-stock-inflection/task.yaml | head -1
echo ""
echo "instruction.md:"
grep -n "$NEW_URL" ../cocoabench-head/fed-rate-cut-stock-inflection/instruction.md | head -1
echo ""
echo "evaluation.md:"
grep -n "$NEW_URL" ../cocoabench-head/fed-rate-cut-stock-inflection/evaluation.md | head -1
echo ""
echo "✨ 全部完成！"
