#!/bin/bash
# 部署番茄钟到 GitHub Pages
set -e

echo "===== 部署番茄钟到 GitHub Pages ====="
echo ""

# Check if gh CLI is available
if ! command -v gh &> /dev/null; then
  echo "需要安装 GitHub CLI。请运行："
  echo "  brew install gh"
  echo "  gh auth login"
  echo ""
  echo "或手动操作："
  echo "  1. 在 github.com 创建新仓库（如 pomodoro）"
  echo "  2. 推送代码："
  echo "     git remote add origin https://github.com/你的用户名/pomodoro.git"
  echo "     git push -u origin main"
  echo "  3. 在仓库 Settings → Pages → Source 选择 main 分支"
  exit 1
fi

# Check if already has remote
if ! git remote get-url origin &>/dev/null 2>&1; then
  read -p "输入你的 GitHub 用户名: " USERNAME
  REPO="pomodoro"

  echo "创建 GitHub 仓库..."
  gh repo create "$REPO" --public --source=. --remote=origin --push
else
  echo "推送代码..."
  git push -u origin main
fi

echo ""
echo "启用 GitHub Pages..."
gh api -X POST "/repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/pages" \
  -f "source[branch]=main" -f "source[path]=/" 2>/dev/null || true

echo ""
echo "✅ 完成！"
echo "几分钟后访问：https://$(gh repo view --json nameWithOwner -q .nameWithOwner | tr '[:upper:]' '[:lower:]').github.io/$(gh repo view --json name -q .name)"
echo ""
echo "手机打开这个网址，添加到主屏幕即可随时使用。"
