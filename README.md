# ⚾ MLB Betting Tracker

Track picks, compare sportsbook odds, and analyze performance — works on iPhone, MacBook, and any device.

---

## 🚀 Deploy to Vercel (2 minutes)

### Step 1 — GitHub
1. Go to [github.com](https://github.com) and sign in (or create a free account)
2. Click the **+** icon → **New repository**
3. Name it `mlb-tracker`, set to **Public**, click **Create repository**
4. Click **uploading an existing file**
5. Upload the entire `mlb-tracker` folder contents (drag the `public/` folder and `vercel.json`)
6. Click **Commit changes**

### Step 2 — Vercel
1. Go to [vercel.com](https://vercel.com) and sign in with GitHub
2. Click **Add New → Project**
3. Find and import your `mlb-tracker` repo
4. Under **Framework Preset** select **Other**
5. Set **Root Directory** to `public`
6. Click **Deploy**

✅ You'll get a URL like `mlb-tracker.vercel.app` — that's your app, live on the internet!

---

## 📱 Add to iPhone Home Screen

1. Open your Vercel URL in **Safari** (must be Safari, not Chrome)
2. Tap the **Share** button (box with arrow pointing up)
3. Scroll down and tap **"Add to Home Screen"**
4. Tap **"Add"**

The app will appear on your home screen with the ⚾ icon, full screen with no browser bar — exactly like a native app.

---

## 💻 Add to MacBook

1. Open the URL in **Safari**
2. Click **File → Add to Dock** (macOS Sonoma+)
   — OR —
   Drag the URL from the address bar to your Dock

---

## 🔑 One-time API key setup

The app uses Claude AI to parse your picks. You need one API key:

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up / log in → click **API Keys** → **Create Key**
3. Copy the key
4. In `public/index.html`, find this line:
   ```
   headers: { 'Content-Type': 'application/json' },
   ```
   Add your key:
   ```
   headers: { 'Content-Type': 'application/json', 'x-api-key': 'YOUR_KEY_HERE', 'anthropic-version': '2023-06-01' },
   ```
5. Re-deploy to Vercel (just push the updated file to GitHub)

---

## ✨ Features

- **Paste any format** — Claude AI parses picks from any website format
- **Auto-calculates** — to-win, P/L, running total all auto-update
- **Best odds** — compares DraftKings, FanDuel, BetMGM, Caesars, PointsBet, ESPN Bet
- **Dashboard** — win rate, ROI, by bet type, by confidence, P/L chart
- **Data persists** — saved to your device (localStorage), survives browser close
- **Export** — download your bet log as CSV anytime
- **Works offline** — service worker caches the app
