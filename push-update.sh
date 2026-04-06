#!/bin/bash
# =====================================================
# MLB Tracker — Push an Edit to GitHub (auto-deploys on Vercel)
# Run this any time you've made a change to index.html:
#   cd ~/Downloads/sportsbetting-tracker
#   ./push-update.sh
# =====================================================

echo "🔍 Checking for changes..."
git status --short

# Stage all changes (index.html and anything else that changed)
git add .

# Check if there's anything to commit
if git diff --cached --quiet; then
  echo "ℹ️  No changes detected — nothing to push."
  exit 0
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M")
git commit -m "Update: $TIMESTAMP"

echo "🚀 Pushing to GitHub..."
git push

echo ""
echo "✅ Pushed! Vercel will auto-deploy in ~30 seconds."
echo "   Check: https://vercel.com/dashboard"
