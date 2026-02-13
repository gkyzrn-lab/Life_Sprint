# 🎮 How to Run Life Sprint Game - Complete Beginner Guide

This guide assumes you have **zero coding experience**. Just follow each step carefully!

---

## 📋 What You Need to Install First

### Step 1: Install Python (The Backend Engine)

1. **Go to**: [python.org/downloads](https://www.python.org/downloads/)
2. **Download**: Click the big yellow button "Download Python 3.14" (or latest version)
3. **Install**: 
   - On Mac: Open the downloaded file, follow the installer
   - **IMPORTANT**: Check the box that says "Add Python to PATH"
4. **Verify**: 
   - Open Terminal (Mac: press `Cmd + Space`, type "Terminal", press Enter)
   - Type: `python3 --version`
   - You should see something like: `Python 3.14.x`

### Step 2: Install Node.js (The Frontend Engine)

1. **Go to**: [nodejs.org](https://nodejs.org/)
2. **Download**: Click the "LTS" (Long Term Support) button
3. **Install**: Open the downloaded file and follow the installer
4. **Verify**: 
   - In Terminal, type: `node --version`
   - You should see something like: `v20.x.x`

---

## 🚀 Running the Game (Every Time You Want to Play)

### Part A: Start the Backend (Game Logic Server)

1. **Open Terminal** (Mac: `Cmd + Space`, type "Terminal")

2. **Navigate to the game folder**:
   ```bash
   cd ~/Desktop/Life_Sprint
   ```

3. **Activate the Python environment** (one-time setup on first run):
   ```bash
   python3 -m venv .venv
   ```
   Then activate it:
   ```bash
   source .venv/bin/activate
   ```
   You'll see `(.venv)` appear at the start of your terminal line.

4. **Install required packages** (only needed first time or after updates):
   ```bash
   pip install -r requirements.txt
   ```
   Wait for it to finish (may take 1-2 minutes).

5. **Start the backend server**:
   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

6. **You should see**:
   ```
   INFO:     Uvicorn running on http://127.0.0.1:8000
   INFO:     Application startup complete.
   ```

7. **Keep this Terminal window open!** The backend is now running.

### Part B: Start the Frontend (Game Interface)

1. **Open a NEW Terminal window** (Mac: `Cmd + N` in Terminal)

2. **Navigate to the frontend folder**:
   ```bash
   cd ~/Desktop/Life_Sprint/life-sprint-frontend
   ```

3. **Install frontend packages** (only needed first time or after updates):
   ```bash
   npm install
   ```
   Wait for it to finish (may take 2-3 minutes).

4. **Start the frontend server**:
   ```bash
   npm run dev
   ```

5. **You should see**:
   ```
   VITE ready in XXX ms
   Local: http://localhost:5173/
   ```

6. **Keep this Terminal window open too!** The frontend is now running.

### Part C: Play the Game!

1. **Open your web browser** (Chrome, Safari, Firefox, etc.)

2. **Go to**: `http://localhost:5173`

3. **🎉 You should see the Life Sprint game!**

---

## 🛑 How to Stop the Game

When you're done playing:

1. Go to **both Terminal windows**
2. Press `Ctrl + C` (on both Mac and Windows)
3. This stops the servers

---

## 🔄 Quick Start (After First Time Setup)

Once you've done the setup above, next time you want to play:

### Terminal 1 (Backend):
```bash
cd ~/Desktop/Life_Sprint
source .venv/bin/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Terminal 2 (Frontend):
```bash
cd ~/Desktop/Life_Sprint/life-sprint-frontend
npm run dev
```

### Browser:
Go to `http://localhost:5173`

---

## ❓ Common Problems & Solutions

### Problem: "python3: command not found"
**Solution**: Python isn't installed or not in PATH. Reinstall Python from python.org and check "Add to PATH".

### Problem: "node: command not found"
**Solution**: Node.js isn't installed. Install from nodejs.org.

### Problem: "No such file or directory"
**Solution**: You're in the wrong folder. Make sure you `cd` to the correct path.

### Problem: "Port 8000 is already in use"
**Solution**: The backend is already running somewhere. Find the other Terminal window and close it, or run:
```bash
lsof -ti:8000 | xargs kill -9
```

### Problem: "Cannot find module..."
**Solution**: Packages aren't installed. Run:
- Backend: `pip install -r requirements.txt`
- Frontend: `npm install`

### Problem: Browser shows "Cannot connect"
**Solution**: Make sure both Terminal windows are running (backend AND frontend).

---

## 🎯 Visual Checklist

- [ ] Python installed and verified (`python3 --version`)
- [ ] Node.js installed and verified (`node --version`)
- [ ] Backend Terminal running (shows "Uvicorn running on...")
- [ ] Frontend Terminal running (shows "VITE ready...")
- [ ] Browser open at `http://localhost:5173`
- [ ] Game visible and playable!

---

## 📞 Still Stuck?

If you're still having issues:
1. Take a screenshot of the error message
2. Note which step you're on
3. Check that both Terminal windows are showing the "running" messages
4. Make sure you didn't close either Terminal window

**Remember**: You need TWO Terminal windows running at the same time - one for backend, one for frontend!
