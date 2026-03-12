# Exercise 4: Memory & Settings

**Time: 30 minutes**

## What You'll Learn

- How Claude Code's memory system works across sessions
- How to configure Claude Code's behaviour with settings
- How permission modes control what Claude Code can do

## Part 1: Memory — Remembering Across Conversations

### The Problem

Every time you start a new Claude Code conversation, it starts fresh. It doesn't remember what you talked about last time. This is by design (for privacy), but sometimes you want Claude Code to remember things — like your preferences, project decisions, or important context.

### How Memory Works

Claude Code has a **memory system** that stores notes in a special folder:

```
~/.claude/
└── projects/
    └── <project-path>/
        └── memory/
            └── MEMORY.md      <-- Main memory file
```

- `MEMORY.md` is loaded at the start of every conversation
- You can ask Claude Code to "remember" things, and it writes them to this file
- You can also create additional memory files for specific topics

### Task 1: Tell Claude Code to Remember Something

Open Claude Code in the workshop project and try:

```
Remember that I prefer snake_case for all Python variable and function names
```

Claude Code should write this to its memory file. Now start a **new conversation** (`/clear`) and ask it to write a function — it should use snake_case without being told.

### Task 2: Check What Claude Code Remembers

You can ask:

```
What do you currently have in your memory?
```

Or look at the file directly. Find it in the file explorer at the path shown above, or ask Claude Code:

```
Show me the contents of your memory file
```

### Task 3: Add More Memories

Try telling Claude Code to remember a few more things:

```
Remember that this is a teaching project and code should be kept simple and well-commented
```

```
Remember that I'm an Australian student so use Australian English spelling (colour, favourite, etc.)
```

### Task 4: Organise Memory

If memory gets long, Claude Code can create separate topic files. For example:

```
Create a separate memory file for my coding preferences
```

This might create something like `~/.claude/projects/.../memory/coding-preferences.md` and link to it from `MEMORY.md`.

### When to Use Memory vs CLAUDE.md

| Use Memory For | Use CLAUDE.md For |
|----------------|-------------------|
| Personal preferences | Project-wide conventions |
| Things you discover during work | Things known upfront |
| Per-user settings | Shared team settings |
| Evolving notes | Stable documentation |

The key difference: **CLAUDE.md is part of the project** (committed to Git, shared with the team). **Memory is personal** (stored on your machine, just for you).

---

## Part 2: Settings — Configuring Claude Code

### What is settings.json?

Claude Code has a settings file that controls its behaviour. There are two levels:

| File | Location | Scope |
|------|----------|-------|
| User settings | `~/.claude/settings.json` | All projects on your machine |
| Project settings | `.claude/settings.json` (in project root) | This project only |

### Task 5: Explore Settings

Ask Claude Code:

```
What settings do you currently have configured? Show me the settings files if they exist.
```

### Task 6: Understand Permission Modes

One of the most important settings is the **permission mode**, which controls what Claude Code is allowed to do without asking:

| Mode | What It Means |
|------|--------------|
| **default** | Claude Code asks permission for most actions (safest) |
| **trusted** | Claude Code can read and edit files without asking, but still asks before running commands |
| **full-auto** | Claude Code can do almost anything without asking (use with caution!) |

In class, we'll use the **default** mode — this way you always see what Claude Code wants to do before it does it.

### Task 7: Look at Settings Options

Here's an example of what a `settings.json` might look like:

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep"
    ],
    "deny": []
  }
}
```

This tells Claude Code it can always read, search, and find files without asking permission, but it still needs to ask before editing files or running commands.

### Task 8: Create a Project Settings File

Let's create a project-level settings file. Ask Claude Code:

```
Create a .claude/settings.json file for this project that allows you to read files and search without asking, but requires permission for edits and bash commands.
```

Review the file it creates. Does it make sense?

---

## Part 3: Understanding How It All Fits Together

Here's how Claude Code loads context when you start a conversation:

```
1. Read ~/.claude/settings.json         (your global settings)
2. Read .claude/settings.json           (project settings)
3. Read CLAUDE.md                       (project instructions)
4. Read CLAUDE.local.md                 (your personal project instructions)
5. Read memory files                    (your personal memories)
6. Ready for your first message!
```

This layered system means:
- **Settings** control what Claude Code *can* do
- **CLAUDE.md** tells Claude Code what it *should* do
- **Memory** gives Claude Code context about *you* and your preferences

## Quick Reference: Key Files

| File | Purpose | Shared? |
|------|---------|---------|
| `CLAUDE.md` | Project instructions for everyone | Yes (committed to Git) |
| `CLAUDE.local.md` | Your personal project instructions | No (gitignored) |
| `~/.claude/settings.json` | Your global Claude Code settings | No (your machine only) |
| `.claude/settings.json` | Project-level Claude Code settings | Yes (committed to Git) |
| `~/.claude/projects/.../memory/` | Your personal memory for this project | No (your machine only) |

## Check Your Understanding

- What's the difference between memory and CLAUDE.md?
- Where are memory files stored?
- What are the three permission modes?
- Why would you use project settings vs user settings?
- In what order does Claude Code load its configuration?

---

**Next up:** [Exercise 5: Build a Python App](../05-build-an-app/README.md)
