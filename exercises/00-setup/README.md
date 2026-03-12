# Exercise 0: Pre-Class Setup

**Complete this before class if possible.** If you run into trouble, don't worry — your instructor can help at the start of class.

## Step 1: Install Git

Git is a version control tool that developers use to track changes to their code. You'll need it to download (clone) this workshop.

### Check if Git is already installed

Open a terminal and type:

```bash
git --version
```

If you see a version number (e.g., `git version 2.43.0`), Git is already installed — skip to **Step 2**.

If you see an error like `command not found`, follow the instructions for your operating system below.

### Windows

1. Download the Git installer from [https://git-scm.com/downloads/win](https://git-scm.com/downloads/win)
2. Run the installer
3. **Important settings during install:**
   - When asked about "Adjusting your PATH environment", select **"Git from the command line and also from 3rd-party software"**
   - For everything else, the default options are fine — just click Next
4. Once installed, **close and reopen your terminal**, then verify:
   ```bash
   git --version
   ```

### macOS

**Option A — Xcode Command Line Tools (simplest):**

Open Terminal and run:

```bash
xcode-select --install
```

A popup will appear asking you to install. Click "Install" and wait for it to finish. Then verify:

```bash
git --version
```

**Option B — Homebrew (if you have it):**

```bash
brew install git
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
```

Then verify:

```bash
git --version
```

### Configure Git (all platforms)

After installing, tell Git who you are (this is used to label your changes):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Use your real name and the email you use for GitHub (or any email — it doesn't need to be verified).

---

## Step 2: Install Visual Studio Code (VS Code)

VS Code is a free code editor. Claude Code runs inside it as an extension.

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com)
2. Download the version for your operating system
3. Install it using the default settings
4. Open VS Code to make sure it launches correctly

### Get comfortable with VS Code

If you haven't used VS Code before, take a minute to find these things:

- **The terminal**: Go to `Terminal` menu > `New Terminal` (or press `` Ctrl+` `` on Windows/Linux, `` Cmd+` `` on macOS)
- **The file explorer**: The icon on the left sidebar that looks like two overlapping files
- **The extensions panel**: The icon on the left sidebar that looks like building blocks (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)

---

## Step 3: Install the Claude Code Extension

1. Open VS Code
2. Open the Extensions panel (`Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Search for **"Claude Code"**
4. Find the extension published by **Anthropic** and click **Install**
5. After installation, you should see a Claude icon in your left sidebar

---

## Step 4: Create an OpenRouter Account

> **If you have a paid Claude/Anthropic subscription**, you can skip this step entirely. Claude Code will work out of the box with your Anthropic account.

OpenRouter gives us access to free AI models that can (mostly) work with Claude Code.

1. Go to [https://openrouter.ai](https://openrouter.ai)
2. Click **Sign Up** and create a free account (no credit card required)
3. Once logged in, go to [https://openrouter.ai/keys](https://openrouter.ai/keys)
4. Click **Create Key**
5. Give it a name like "claude-code-workshop"
6. **Copy your API key** — it will look like `sk-or-v1-abc123...`
7. **Save this key somewhere safe** (e.g., a text file on your desktop). You won't be able to see it again after leaving the page.

> **Security note:** Your API key is like a password. Don't share it with others or post it online.

---

## Step 5: Configure Claude Code to Use OpenRouter

Now we need to tell Claude Code to use your OpenRouter key instead of a paid Anthropic account.

### Windows

1. Open VS Code
2. Open the terminal inside VS Code (`Terminal` > `New Terminal`)
3. In the terminal, run these commands **one at a time**, replacing `YOUR_KEY_HERE` with the API key you copied:

```powershell
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://openrouter.ai/api", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_AUTH_TOKEN", "YOUR_KEY_HERE", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_DEFAULT_SONNET_MODEL", "google/gemini-2.5-pro-exp-03-25:free", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_DEFAULT_HAIKU_MODEL", "google/gemini-2.5-pro-exp-03-25:free", "User")
```

4. **Close and reopen VS Code** for the changes to take effect

### macOS

1. Open VS Code
2. Open the terminal inside VS Code (`Terminal` > `New Terminal`)
3. Run this command, replacing `YOUR_KEY_HERE` with your API key:

```bash
cat >> ~/.zshrc << 'EOF'

# Claude Code + OpenRouter Configuration
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="YOUR_KEY_HERE"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_DEFAULT_SONNET_MODEL="google/gemini-2.5-pro-exp-03-25:free"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="google/gemini-2.5-pro-exp-03-25:free"
EOF
```

Then replace YOUR_KEY_HERE in the file:

```bash
nano ~/.zshrc
```

Use arrow keys to find `YOUR_KEY_HERE`, replace it with your actual key, then press `Ctrl+X`, then `Y`, then `Enter` to save.

4. Load the new settings:

```bash
source ~/.zshrc
```

5. **Close and reopen VS Code** for the changes to take effect

### Linux

Follow the same steps as macOS, but if you use bash instead of zsh, replace `~/.zshrc` with `~/.bashrc`.

---

## Step 6: Verify Everything Works

1. Open VS Code
2. Open a terminal inside VS Code
3. Run the verification script (we'll do this together in class):

```bash
python3 exercises/00-setup/verify_setup.py
```

Or simply try opening the Claude Code panel in VS Code and sending a simple message like "Hello, what model are you?"

### Troubleshooting

| Problem | Solution |
|---------|----------|
| "command not found: git" | Git isn't installed or your terminal needs restarting. Close and reopen your terminal. |
| Claude Code extension not showing | Make sure you installed the one by **Anthropic**. Try restarting VS Code. |
| Claude Code says "authentication failed" | Check that your `ANTHROPIC_API_KEY` is set to an empty string `""` (not unset). Restart VS Code. |
| Claude Code seems to hang | The free model may be slow. Give it 30 seconds. If it still doesn't respond, try sending a simpler message. |
| "Rate limit exceeded" | You've hit the free tier limit. Wait a minute and try again, or use shorter/simpler prompts. |

---

## What You Should Have When Done

- [ ] Git installed and configured
- [ ] VS Code installed
- [ ] Claude Code extension installed in VS Code
- [ ] OpenRouter account with an API key
- [ ] Environment variables configured
- [ ] (Optional) Verified with a test message

**You're ready for class!**
