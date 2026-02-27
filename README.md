# Life_Sprint

A productivity and life management application.

## Getting Started

### For Contributors (Forking Workflow)

To contribute to this project:

1. Fork this repository on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Life_Sprint.git
   cd Life_Sprint
   ```
3. Add upstream remote (to sync with the original repository):
   ```bash
   git remote add upstream https://github.com/gkyzrn-lab/Life_Sprint.git
   ```
4. Make your changes, commit them, and push to your fork:
   ```bash
   git push -u origin main
   ```

### For Connecting a Local Repository

If you have initialized a local repository and want to connect it to GitHub:

```bash
git remote add origin https://github.com/YOUR_USERNAME/Life_Sprint.git
git push -u origin main
```

### For Direct Cloning

To simply use or explore this repository:

```bash
git clone https://github.com/gkyzrn-lab/Life_Sprint.git
cd Life_Sprint
```

## Pushing Your Code from Visual Studio Code

If you have your project open in Visual Studio Code and want to push it to this GitHub repository, follow these steps:

### Option 1: Using the VS Code Source Control Panel (GUI)

1. Open your project folder in VS Code
2. Click the **Source Control** icon in the left sidebar (or press `Ctrl+Shift+G` / `Cmd+Shift+G` on Mac)
3. If not already a git repository, click **Initialize Repository**
4. Stage your files by clicking the **+** icon next to each file, or click **+** next to "Changes" to stage all
5. Enter a commit message in the text box and click the **✓ (checkmark)** to commit
6. Click the **...** menu → **Remote** → **Add Remote**, then enter:
   - Remote name: `origin`
   - URL: `https://github.com/gkyzrn-lab/Life_Sprint.git`
7. Click **Publish Branch** (or use **...** menu → **Push**)

### Option 2: Using the VS Code Integrated Terminal

Open the terminal in VS Code (`` Ctrl+` `` / `` Cmd+` `` on Mac) and run:

```bash
# Initialize git (if not already done)
git init

# Stage all your files
git add .

# Commit your changes
git commit -m "Add my project files"

# Connect to the remote repository
git remote add origin https://github.com/gkyzrn-lab/Life_Sprint.git

# Pull any existing remote content first (if the remote already has commits)
git pull origin main --rebase

# Push your code
git push -u origin main
```

> **Note:** If your default branch is named `master` instead of `main`, replace `main` with `master` in the commands above.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.