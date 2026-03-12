# Exercise 5: Build a Python App with Claude Code

**Time: 60 minutes**

## What You'll Learn

- How to iteratively build an application using Claude Code
- How to write a CLAUDE.md before you start coding
- How to ask Claude Code to write tests
- How to debug and fix issues with Claude Code's help
- The "prompt, review, approve, test" workflow

## What We're Building

A **command-line to-do list application** that lets you:
- Add tasks
- List all tasks
- Mark tasks as complete
- Delete tasks
- Save tasks to a file so they persist between runs

We'll build this step-by-step, with Claude Code doing the coding while you guide it.

## Setup

1. Open the starter folder in VS Code:
   ```bash
   cd exercises/05-build-an-app/starter
   code .
   ```
   Or open `exercises/05-build-an-app/starter` via `File` > `Open Folder`.

2. Have a look at the starter file — it's just a skeleton to get us going.

> **Tip:** If you're using a free model and it struggles with a large request, break it into smaller pieces. Instead of "build the whole app", try one feature at a time.

## Step 1: Write CLAUDE.md First

Before writing any code, let's set up a CLAUDE.md. Create a file called `CLAUDE.md` in the `starter` folder with:

```markdown
# Todo List CLI Application

A simple command-line to-do list application built in Python.

## Tech Stack

- Python 3.8+
- No external dependencies (standard library only)
- Data stored in JSON format in a file called `todos.json`

## Conventions

- Use snake_case for all functions and variables
- Each function should have a docstring
- Keep functions short and focused (one job each)
- Use type hints where practical
- Handle errors gracefully with user-friendly messages

## Project Structure

- `todo.py` - Main application (CLI interface)
- `todo_manager.py` - Business logic (add, remove, complete, list tasks)
- `test_todo.py` - Tests

## How to Run

```bash
python3 todo.py
```

## How to Test

```bash
python3 -m pytest test_todo.py -v
```
```

## Step 2: Build the Data Layer

Ask Claude Code to create the task manager:

```
Create todo_manager.py with a TodoManager class that can:
- Load and save todos from/to a JSON file (todos.json)
- Add a new todo with a title (auto-assign an ID and set status to "pending")
- List all todos
- Mark a todo as complete by ID
- Delete a todo by ID

Each todo should be a dict with: id (int), title (str), status (str: "pending" or "complete"), created (ISO timestamp string)
```

**Review the code carefully before approving!** Check:
- Does it follow the conventions in your CLAUDE.md?
- Does the JSON saving/loading look correct?
- Are there docstrings?

## Step 3: Write Tests

Now let's ask Claude Code to write tests:

```
Create test_todo.py with pytest tests for the TodoManager class. Test each method: add_todo, list_todos, complete_todo, delete_todo, and the save/load functionality. Use a temporary file for testing so we don't mess up real data.
```

**Run the tests:**

```
Run the tests and show me the results
```

Or run them yourself:

```bash
python3 -m pytest test_todo.py -v
```

If any tests fail, ask Claude Code to fix them:

```
These tests are failing. Can you look at the errors and fix the issues?
```

## Step 4: Build the CLI Interface

Now let's create the user interface:

```
Update todo.py to be a command-line interface for the TodoManager. It should show a menu:
1. Add task
2. List tasks
3. Complete task
4. Delete task
5. Quit

Use a loop so the user can keep performing actions until they choose to quit.
```

**Test it manually:**

```
Run todo.py so I can try it out
```

Try adding a few tasks, listing them, completing one, and deleting one.

## Step 5: Improve It

Now that the basic app works, let's iterate. Try asking for improvements one at a time:

### Add colour to the output

```
Add colour to the CLI output using ANSI escape codes (no external libraries).
Make completed tasks show in green and pending tasks show in yellow.
```

### Add a search feature

```
Add option 6 to the menu: "Search tasks". It should let the user type a keyword and show all tasks that contain that keyword in the title.
```

### Add due dates (stretch goal)

```
Add an optional due date when creating a task. When listing tasks, show how many days until the due date (or how many days overdue). Format dates as DD/MM/YYYY.
```

## Step 6: Run All Tests Again

After all the changes:

```
Run the full test suite. If any tests are failing because of our new features, update the tests to cover the new functionality too.
```

## The Workflow You Just Practised

This exercise demonstrated the core Claude Code workflow for building software:

```
1. Plan       → Write CLAUDE.md with conventions and structure
2. Build      → Ask Claude Code to create code, one piece at a time
3. Review     → Read the proposed changes before approving
4. Test       → Ask Claude Code to write and run tests
5. Iterate    → Add features, fix bugs, improve
6. Verify     → Run tests after every change
```

This cycle of **prompt → review → approve → test** is how developers use Claude Code in real projects.

## Common Issues and Tips

| Problem | Solution |
|---------|----------|
| Claude Code writes too much at once | Break your request into smaller, specific pieces |
| Tests fail after adding a feature | Ask Claude Code to update the tests for the new feature |
| The code doesn't match your CLAUDE.md conventions | Point out what's wrong: "This function doesn't have a docstring — our CLAUDE.md says they should" |
| Free model is struggling | Simplify your prompts. Instead of "add colour and search", do one at a time |
| App crashes with an error | Paste the error into Claude Code: "I'm getting this error when I try to add a task: [error]" |

## Check Your Understanding

- Why did we write CLAUDE.md before writing any code?
- What's the benefit of asking Claude Code to write tests?
- Why is it important to review code before approving changes?
- How do you handle it when Claude Code's changes break something?
- What's the difference between asking for one feature at a time vs everything at once?

---

**Next up:** [Exercise 6: Advanced Features](../06-advanced-features/README.md)
