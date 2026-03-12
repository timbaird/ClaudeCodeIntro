# Exercise 3: CLAUDE.md — Teaching Claude About Your Project

**Time: 30 minutes**

## What You'll Learn

- What a `CLAUDE.md` file is and why it matters
- How `CLAUDE.md` changes Claude Code's behaviour
- How to write an effective `CLAUDE.md` for a project

## What is CLAUDE.md?

When you start a conversation, Claude Code automatically looks for a file called `CLAUDE.md` in your project's root folder. If it finds one, it reads it **before** your first message.

Think of `CLAUDE.md` as a **briefing document** for Claude Code. It tells Claude:

- What this project is about
- What conventions or rules to follow
- What technologies are used
- Any important things to keep in mind

Without a `CLAUDE.md`, Claude Code has to figure all of this out from scratch every time. With one, it starts the conversation already understanding your project.

## Task 1: See the Difference Without CLAUDE.md

First, let's see what happens when Claude Code has no `CLAUDE.md`.

1. Open VS Code in the `mystery_project` folder:
   ```bash
   cd exercises/03-claude-md/mystery_project
   code .
   ```
   Or open the folder using `File` > `Open Folder` in VS Code.

2. Open Claude Code and ask:
   ```
   What is this project? Give me a quick summary.
   ```

3. Notice how Claude Code has to:
   - Read multiple files to understand the project
   - Take time to piece together what it does
   - May get some details slightly wrong

4. Now ask:
   ```
   Add a function to find the top performing student
   ```

   Notice the choices Claude Code makes — it has to guess about:
   - Which file to put the function in
   - What coding style to use
   - Whether to use Australian grading terms (HD, D, C, P, F) or American ones (A, B, C, D, F)

## Task 2: Write a CLAUDE.md

Now let's create a `CLAUDE.md` file that gives Claude Code context about this project.

Create a new file called `CLAUDE.md` in the `mystery_project` folder. You can do this in VS Code by right-clicking in the file explorer and selecting "New File", or ask Claude Code:

```
Create a CLAUDE.md file in the current directory
```

But wait — let's write it **ourselves** first so we understand what goes in it. Open the file and write something like this (feel free to use your own words):

```markdown
# Student Grade Tracker

A Python application that tracks and reports student grades using the Australian grading system.

## Project Structure

- `app.py` - Main application logic (grade calculation, reports)
- `data.py` - Student data and grade boundary definitions
- `utils.py` - Helper/utility functions

## Conventions

- Uses Australian university grading: HD (High Distinction), D (Distinction), C (Credit), P (Pass), F (Fail)
- Grade boundaries are defined in data.py and should not be hardcoded elsewhere
- All averages should be rounded to 1 decimal place
- Student names are formatted as "First Last"
- New functions should include a docstring explaining what they do
- Code should be kept simple — this is a teaching project

## How to Run

```bash
python3 app.py
```
```

Save the file.

## Task 3: See the Difference With CLAUDE.md

Now **start a new Claude Code conversation** (you may need to close and reopen the Claude panel, or use the `/clear` command to start fresh).

Ask the same questions:

```
What is this project? Give me a quick summary.
```

**What to notice:**
- Claude Code already knows what the project is about
- It mentions the Australian grading system without having to read the data file
- Its response is faster and more accurate

Now ask:

```
Add a function to find the top performing student
```

**What to notice:**
- Claude Code follows the conventions in your `CLAUDE.md`
- It adds a docstring (because we asked for that in conventions)
- It uses the correct grading terminology
- It puts the function in a logical place

## Task 4: Experiment With CLAUDE.md

Try modifying your `CLAUDE.md` and seeing how it affects Claude Code's behaviour.

### Experiment A: Add a style rule

Add this to your `CLAUDE.md`:

```markdown
## Style Rules

- Always use snake_case for function names
- Print output should use f-strings, not .format() or concatenation
- Never use single-letter variable names (use descriptive names instead)
```

Start a new conversation and ask Claude Code to add a feature. Does it follow your style rules?

### Experiment B: Add warnings

Try adding:

```markdown
## Important

- Do NOT modify data.py — the student data is read-only
- Do NOT change the grade boundaries
```

Now ask Claude Code to change the pass mark to 50. Does it respect your warning?

## What Makes a Good CLAUDE.md?

| Do | Don't |
|----|-------|
| Explain what the project does in 1-2 sentences | Write an essay — keep it concise |
| List the key files and what they contain | List every single file |
| State coding conventions clearly | Assume Claude Code will guess your preferences |
| Include how to run/test the project | Include obvious things ("this is a Python file") |
| Mention important constraints or rules | Overload it with too many rules |

## Where Can CLAUDE.md Files Live?

Claude Code looks for `CLAUDE.md` in several places:

| Location | Scope |
|----------|-------|
| `~/CLAUDE.md` | Applies to **all** your projects (personal preferences) |
| `./CLAUDE.md` (project root) | Applies to **this project** for all users |
| `./CLAUDE.local.md` | Applies to **this project** for just you (not committed to Git) |
| `./src/CLAUDE.md` (subdirectory) | Applies when working in that subdirectory |

For team projects, `CLAUDE.md` is committed to Git so everyone shares the same conventions. `CLAUDE.local.md` is for your personal preferences and should be added to `.gitignore`.

## Check Your Understanding

- What is the purpose of a `CLAUDE.md` file?
- Where does Claude Code look for `CLAUDE.md`?
- What's the difference between `CLAUDE.md` and `CLAUDE.local.md`?
- How did Claude Code's behaviour change after you added the `CLAUDE.md`?
- Why is it better to write conventions in `CLAUDE.md` rather than repeating them in every conversation?

---

**Next up:** [Exercise 4: Memory & Settings](../04-memory-and-settings/README.md)
