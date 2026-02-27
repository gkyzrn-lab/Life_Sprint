# Store System - Quick Test Checklist

## ✅ Frontend Integration Complete

### What's New:
- **Store Tab** added to GameBoard navigation (🛍️ icon)
- **StorePanel.tsx** component displays all 18 purchases
- **Beautiful UI** with categories, filters, and animations
- **Real API integration** connecting to backend endpoints

---

## 🚀 Quick Start (Right Now!)

### Servers Running ✓
- Backend: `http://localhost:8000` (FastAPI)  
- Frontend: `http://localhost:3000` (React)

### What to Do:
1. **Open** `http://localhost:3000` in your browser
2. **Enter** a player name
3. **Click** the 🛍️ **Store** tab
4. **Buy** something (if you have money)!

---

## 📋 Test Scenarios

### Scenario 1: Browse Purchases
- Click Store tab
- See grid of 18 purchases
- Use category buttons to filter
- ✅ Each purchase shows emoji, name, cost, effects

### Scenario 2: Make a Purchase
- Find an affordable item (green button)
- Click "Buy Now"
- See ✅ confirmation message
- Check balance decreased
- ✅ Success!

### Scenario 3: Afford Check
- Find expensive item (red disabled button)
- Try to click "Buy Now"
- Button is disabled (can't click)
- ✅ System prevents bankruptcy

### Scenario 4: Smart Suggestions
- Click "Suggestions" tab
- See personalized recommendations
- Each shows a reason (e.g., "Your stress is high...")
- ✅ AI-powered recommendations working

### Scenario 5: Track Purchases
- Click "History" tab
- See your past purchases
- View the effects applied
- ✅ Purchase history tracked

---

## 🎯 18 Purchases Available

| # | Name | Cost | Category | Effects |
|---|------|------|----------|---------|
| 1 | Coffee with friends | $15 | Social | Happiness +20 |
| 2 | Dinner with roommates | $40 | Social | Happiness +25, Stress -10 |
| 3 | Weekend trip | $150 | Social | Happiness +35, Stress -15 |
| 4 | Networking event | $35 | Social | Network +30 |
| 5 | Sports event | $50 | Social | Health +15, Happiness +10 |
| 6 | Gym membership | $30 | Health | Health +25, Fitness +20 |
| 7 | Protein smoothie | $8 | Health | Health +10, Energy +15 |
| 8 | Doctor's checkup | $100 | Health | Health +20 |
| 9 | Gas/Uber rides | $20 | Practical | Convenience |
| 10 | Phone bill | $50 | Practical | Essential |
| 11 | Books for class | $40 | Practical | GPA +5 |
| 12 | Massage | $60 | Self-Care | Stress -30, Happiness +15 |
| 13 | Spa day | $80 | Self-Care | Stress -40, Happiness +20 |
| 14 | Therapy session | $120 | Self-Care | Mental Health +30 |
| 15 | Video game | $60 | Fun | Fun +25, Happiness +10 |
| 16 | Concert tickets | $80 | Fun | Happiness +30, Energy +10 |
| 17 | Meditation app | $10 | Wellness | Stress -15 |
| 18 | Vitamin supplements | $25 | Wellness | Health +20 |

---

## 🔧 If Something's Wrong

**Store tab not showing?**
```bash
# Restart frontend
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend
npm run dev
```

**Purchases not loading?**
```bash
# Check backend
ps aux | grep uvicorn
# Should see: /Library/Frameworks/Python.framework/... uvicorn main:app --reload
```

**Backend not running?**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Clear cache**
```bash
# Hard refresh in browser
Cmd + Shift + R  (Mac)
Ctrl + Shift + R (Windows/Linux)
```

---

## 📊 Files Modified/Created

### Frontend:
- ✅ `src/components/StorePanel.tsx` - Store UI component
- ✅ `src/components/StorePanel.css` - Store styling  
- ✅ `src/components/GameBoard.tsx` - Added store tab

### Backend (Already Working):
- ✅ `catalogs/life_purchases.py` - 18 purchases
- ✅ `store/purchase_service.py` - Purchase logic
- ✅ `api/router_store.py` - API endpoints
- ✅ `main.py` - Router integrated

---

## ✨ Features

| Feature | Status | Details |
|---------|--------|---------|
| Display 18 purchases | ✅ | Grid layout with emojis |
| Category filtering | ✅ | 6 categories to filter by |
| Affordability check | ✅ | Green if can afford, red if not |
| Make purchases | ✅ | Calls POST /api/store/purchase |
| Show effects | ✅ | Displays stat changes |
| Smart suggestions | ✅ | AI recommends based on stats |
| Purchase history | ✅ | Shows past purchases |
| Balance tracking | ✅ | Updates after each purchase |
| Responsive design | ✅ | Works on mobile too |

---

## 🎉 You're All Set!

Everything is integrated and ready. Your money spending is now:
- ✅ Responsive to your actions
- ✅ Connected to real-life purchases
- ✅ Showing meaningful effects on your stats
- ✅ Tracked with smart recommendations

**Go test it!** `http://localhost:3000` → Click 🛍️ Store
