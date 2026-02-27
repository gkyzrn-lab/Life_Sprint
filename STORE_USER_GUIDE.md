# 🛍️ Store System - User Guide

## Getting Started

### Prerequisites
- Both servers running (already started for you)
- Browser open to `http://localhost:3000`
- Player created in the game

---

## Finding the Store

1. **Open the app**: Go to `http://localhost:3000`
2. **Enter your name**: Type your player name
3. **Start the game**: Click start
4. **Open GameBoard**: You'll see the main game interface
5. **Click Store**: Look for the 🛍️ icon in the navigation tabs
6. **Explore**: Browse 18 real-life purchases!

---

## Understanding the Store

### The Navigation Tabs
At the top of the store, you'll see three tabs:
- **Available** - Browse all 18 items you can buy
- **Suggestions** - See AI recommendations based on your stats
- **History** - View purchases you've made this semester

### Your Balance
Top-right shows your current money: `Balance: $X.XX`
- This is what you can spend
- Updates immediately after each purchase
- Can't spend more than you have

---

## Browsing Purchases

### Category Buttons
Use the buttons at the top to filter by category:
- **All** - See every item
- **Social** - Coffee, dinner, events, trips
- **Health** - Gym, food, checkups
- **Practical** - Transportation, bills, books
- **Self-Care** - Massage, spa, therapy
- **Fun** - Games, concerts
- **Wellness** - Meditation, supplements

### Reading a Purchase Card

Each purchase shows:
```
📱 Example Item
"This is what the item does..."
$49.99
┌─────────────────────┐
│ Happiness: +25      │
│ Stress: -10         │
│ Energy: +5          │
└─────────────────────┘
[ Buy Now ] or [ Too Expensive ]
```

**What each element means:**
- **Emoji** - Visual icon for the item
- **Name** - What you're buying
- **Description** - Why you'd want it
- **Cost** - How much money it takes
- **Effects** - How it changes your stats
- **Button** - Click to buy (if you can afford it)

### Affordability
- **Green button** - You have enough money
- **Gray/Disabled button** - Too expensive for your budget

---

## Making a Purchase

### Step 1: Find Something You Want
Browse through available items and find one that interests you.

### Step 2: Check the Cost
Make sure you have enough money. Look at your balance in the top-right.
- If balance > cost = ✅ You can buy it
- If balance < cost = ❌ Too expensive

### Step 3: Click "Buy Now"
The purchase will process and you'll see:
- ✅ Green confirmation message
- Your balance will decrease
- The purchase is recorded

### Step 4: See the Effects
Your player stats will update based on the purchase effects:
- **Happiness might increase** (social items)
- **Stress might decrease** (self-care items)
- **Health might improve** (fitness items)
- And more based on what you bought!

### Example Purchases

**Feeling stressed? Buy a massage**
- Cost: $60
- Effects: Stress -30, Happiness +15
- Result: Much less stressed, feeling happy!

**Need to improve health? Buy gym membership**
- Cost: $30
- Effects: Health +25, Fitness +20
- Result: Way healthier and fit!

**Want to have fun? Get concert tickets**
- Cost: $80
- Effects: Happiness +30, Energy +10
- Result: Super happy and energized!

---

## Using the Suggestions Tab

### What Are Suggestions?
The AI looks at your current stats and recommends items that would help you most.

### Why Different Suggestions?
Based on YOUR situation:
- High stress? → Suggests relaxing items (massage, spa, yoga)
- Low happiness? → Suggests fun items (concert, games, friends)
- Poor health? → Suggests fitness/wellness items
- Low network? → Suggests social items (events, coffee, dinner)

### How to Use Them
1. Click **Suggestions** tab
2. Read the recommendation and reason
3. Click **Buy Now** if interested
4. Or go back to **Available** to keep browsing

### Understanding the Reason
Each suggestion includes a reason:
- "Your stress is high..." → They noticed you need stress relief
- "Your happiness is low..." → They noticed you need cheering up
- "Your health is poor..." → They noticed you need to exercise
- etc.

---

## Checking Your History

### What's in History?
Every purchase you've ever made appears here, showing:
- **Item name** - What you bought
- **Cost** - How much you paid
- **Semester** - When you bought it
- **Effects** - What changed in your stats

### Why Check History?
- **See patterns** - Are you spending too much? Too little?
- **Remember purchases** - Did I buy this before?
- **Track impact** - How did purchases affect my stats?
- **Plan better** - What should I buy next semester?

### Reading History Items
```
💰 Item Name                                      -$XX.XX
   Semester 1
   ├─ Happiness: +25
   ├─ Stress: -10
   └─ Energy: +5
```

---

## Tips for Smart Spending

### ✅ Do This:
- **Check your balance** before buying
- **Read the effects** to understand impact
- **Use suggestions** for personalized advice
- **Track history** to avoid buying same thing twice
- **Buy strategically** to improve your weakest stats
- **Try suggestions** - they're based on AI analysis
- **Spread purchases** - don't blow all money at once

### ❌ Don't Do This:
- **Overspend** - You can't spend more than you have
- **Ignore suggestions** - They're smart!
- **Buy the same item repeatedly** - Use once per semester
- **Forget affordability** - Disabled buttons mean you can't afford it
- **Neglect your stats** - Use purchases to improve weak areas

---

## Strategic Examples

### Scenario 1: Your Stress is 90% (VERY HIGH)
**What the system suggests:**
- Massage ($60) - Stress -30 ⭐
- Spa day ($80) - Stress -40 ⭐⭐
- Therapy session ($120) - Mental health +30 ⭐⭐⭐

**What you should do:**
- If low budget: Buy massage
- If medium budget: Buy spa day
- If high budget: Buy therapy session (most effective!)

### Scenario 2: Your Health is 30% (LOW)
**What the system suggests:**
- Gym membership ($30) - Health +25
- Doctor checkup ($100) - Health +20
- Protein smoothie ($8) - Health +10

**What you should do:**
- Start with protein smoothies (cheap, builds momentum)
- Then gym membership (long-term benefit)
- Doctor checkup if still needed

### Scenario 3: Your Happiness is 20% (VERY LOW)
**What the system suggests:**
- Coffee with friends ($15) - Happiness +20
- Dinner with roommates ($40) - Happiness +25
- Weekend trip ($150) - Happiness +35 (BEST!)

**What you should do:**
- If low budget: Coffee with friends
- If medium budget: Dinner with roommates
- If high budget: Weekend trip (biggest happiness boost!)

---

## All 18 Items Reference

### Social (5 items)
| Item | Cost | Main Effect |
|------|------|------------|
| Coffee with friends | $15 | Happiness +20 |
| Dinner with roommates | $40 | Happiness +25 |
| Weekend trip | $150 | Happiness +35 |
| Networking event | $35 | Network +30 |
| Sports event | $50 | Health +15 |

### Health (3 items)
| Item | Cost | Main Effect |
|------|------|------------|
| Gym membership | $30 | Health +25 |
| Protein smoothie | $8 | Health +10 |
| Doctor's checkup | $100 | Health +20 |

### Practical (3 items)
| Item | Cost | Main Effect |
|------|------|------------|
| Gas/Uber rides | $20 | Essential |
| Phone bill | $50 | Essential |
| Books for class | $40 | GPA +5 |

### Self-Care (3 items)
| Item | Cost | Main Effect |
|------|------|------------|
| Massage | $60 | Stress -30 |
| Spa day | $80 | Stress -40 |
| Therapy session | $120 | Mental health +30 |

### Fun (2 items)
| Item | Cost | Main Effect |
|------|------|------------|
| Video game | $60 | Fun +25 |
| Concert tickets | $80 | Happiness +30 |

### Wellness (2 items)
| Item | Cost | Main Effect |
|------|------|------------|
| Meditation app | $10 | Stress -15 |
| Vitamin supplements | $25 | Health +20 |

---

## FAQ

**Q: Can I buy the same item multiple times?**
A: Yes for some items (coffee, gym), but limited one-time items reset next semester.

**Q: What if I don't have enough money?**
A: The button will be disabled (gray). You need to earn more or buy something cheaper.

**Q: Do purchases affect my final stats?**
A: Yes! They permanently modify your player stats for the semester.

**Q: Can I undo a purchase?**
A: No, but you can check your history to learn what worked well.

**Q: How often can I access the store?**
A: Whenever you want! Click the Store tab anytime.

**Q: Are suggestions always right?**
A: They're smart recommendations based on your stats, but you decide!

**Q: Do I lose money at end of semester?**
A: Purchases are permanent, but you earn more money next semester.

**Q: What's the best strategy?**
A: Buy what improves your weakest stats, use suggestions for guidance!

---

## Keyboard Shortcuts

None built-in, but you can:
- Use **Tab key** to navigate buttons
- Use **Enter key** to click buttons
- Press **F12** to see developer console if errors occur

---

## Getting Help

### Common Issues

**Can't see purchases loading?**
- Wait a moment (API call takes a second)
- Check your internet connection
- Try refreshing (Cmd+Shift+R on Mac)

**Buy button not responding?**
- Make sure you have enough money
- Check browser console (F12) for errors
- Try clicking again

**Balance not updating?**
- Refresh the page to see latest balance
- Check purchase history to confirm it went through

**Suggestions not showing?**
- You might already have ideal stats (rare!)
- Try playing more to change your stats
- Then check suggestions again

---

## Have Fun! 🎉

The store is designed to make spending money feel meaningful and fun!
- Explore different purchases
- Try out AI suggestions
- See how purchases affect your stats
- Manage your budget wisely
- Complete your semester successfully

**Happy shopping!** 🛍️
