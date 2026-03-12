# Exercise 1: Git Basics & Cloning This Workshop

**Time: 30 minutes**

## What You'll Learn

- What Git and GitHub are and why developers use them
- How to clone (download) a repository
- How to navigate a project in VS Code

## What is Git?

Git is a **version control system**. Think of it as an unlimited "undo" history for your entire project. Every time you save a snapshot (called a **commit**), Git remembers exactly what every file looked like at that point.

This means you can:
- Go back to any previous version of your code
- See exactly what changed and when
- Work on new features without breaking what already works

## What is GitHub?

**GitHub** is a website that hosts Git repositories (projects) online. It's like Google Drive for code — except it also tracks every change ever made.

- **Git** = the tool that tracks changes (runs on your computer)
- **GitHub** = the website that stores and shares those changes (in the cloud)

## Task 1: Clone This Workshop Repository

"Cloning" means downloading a copy of a repository from GitHub to your computer.

1. Open VS Code
2. Open the terminal (`Terminal` > `New Terminal` or press `` Ctrl+` ``)
3. Navigate to where you want to store the workshop. For example:

```bash
cd ~/Documents
```

4. Clone the repository:

```bash
git clone <REPO_URL_PROVIDED_BY_INSTRUCTOR>
```

> Your instructor will give you the actual URL. It will look something like:
> `https://github.com/username/claude-code-workshop.git`

5. Open the cloned folder in VS Code:

```bash
code claude-code-workshop
```

Or use `File` > `Open Folder` and navigate to the `claude-code-workshop` folder.

## Task 2: Explore the Repository

Now that you have the project open in VS Code, let's look around.

1. **Look at the file explorer** (left sidebar). You should see a folder structure like:
   ```
   claude-code-workshop/
   ├── README.md
   ├── exercises/
   │   ├── 00-setup/
   │   ├── 01-git-basics/     <-- You are here!
   │   ├── 02-first-conversation/
   │   └── ...
   └── solutions/
   ```

2. **Click on `README.md`** in the root of the project. This is the workshop overview.

3. **Click on different folders** to see what's inside them.

## Task 3: Basic Git Commands

Let's try a few Git commands in the terminal to see what Git knows about this project.

### See the status of your repository

```bash
git status
```

This tells you which files have changed. Right now it should say "nothing to commit, working tree clean" because you haven't changed anything yet.

### See the history of changes

```bash
git log --oneline
```

This shows a list of commits (snapshots) that were made to this project. Each line is one commit, with a short description.

### Make a change and see Git notice it

1. Open `exercises/01-git-basics/README.md` (this file!) in VS Code
2. Add a blank line at the very bottom of the file
3. Save the file (`Ctrl+S` / `Cmd+S`)
4. Run `git status` again in the terminal

You should see that Git has noticed your change! It will say something like:
```
modified: exercises/01-git-basics/README.md
```

### Undo your change

Since we don't actually want to keep that change:

```bash
git checkout -- exercises/01-git-basics/README.md
```

Run `git status` again — the change is gone, and the file is back to its original state.

## Key Concepts to Remember

| Concept | What It Means |
|---------|--------------|
| **Repository (repo)** | A project folder tracked by Git |
| **Clone** | Download a copy of a repository |
| **Commit** | A saved snapshot of your project at a point in time |
| **Status** | Check what's changed since the last commit |
| **Working tree clean** | Nothing has changed — everything matches the last commit |

## Check Your Understanding

- What's the difference between Git and GitHub?
- What does `git clone` do?
- What does `git status` tell you?
- Why is version control useful?

---

**Next up:** [Exercise 2: Your First Conversation with Claude Code](../02-first-conversation/README.md)
