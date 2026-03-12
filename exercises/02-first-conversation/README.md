# Exercise 2: Your First Conversation with Claude Code

**Time: 30 minutes**

## What You'll Learn

- How to open and use Claude Code in VS Code
- How to ask Claude Code to explain code
- How to ask Claude Code to modify code
- How to approve or reject changes Claude Code suggests
- The difference between asking questions and giving instructions

## Getting Started

1. Make sure you have the `claude-code-workshop` folder open in VS Code
2. Open the Claude Code panel by clicking the Claude icon in the left sidebar
3. You should see a chat input at the bottom of the panel

> **Using a free model?** Remember, free models may occasionally give odd responses or struggle with tool calls. If something seems wrong, try rephrasing your request in simpler terms. This is a limitation of the free model, not something you're doing wrong.

## Task 1: Say Hello

In the Claude Code chat, type:

```
Hello! What model are you running as?
```

This is a simple test to confirm Claude Code is working. It should respond conversationally and tell you which model it's using.

**What to notice:**
- Claude Code responds in the chat panel
- It can have natural conversations, not just code

## Task 2: Ask Claude Code to Explain Code

Let's ask Claude Code about the starter code in this exercise.

Type this into the Claude Code chat:

```
Can you read the file exercises/02-first-conversation/starter_code/greeting.py and explain what it does?
```

**What to notice:**
- Claude Code uses a **Read** tool to actually open the file
- You may see a permission prompt — click **Allow** to let it read the file
- It then explains the code in plain language

### Follow-up questions to try:

```
What does the f before the string in the greet function mean?
```

```
What would happen if I passed an empty list to greet_multiple?
```

These show that Claude Code can answer follow-up questions and remembers the context of your conversation.

## Task 3: Ask Claude Code to Explain More Complex Code

Now let's look at the calculator:

```
Read exercises/02-first-conversation/starter_code/calculator.py and explain the calculate function. What pattern is it using?
```

**What to notice:**
- Claude Code can identify programming patterns (this one uses if/elif chaining)
- It explains not just *what* the code does, but *how* it works

## Task 4: Ask Claude Code to Modify Code

Now let's get Claude Code to actually change some code. Type:

```
Add a power/exponent operator (using **) to the calculator.py file. The operator should be "^".
```

**What to notice:**
- Claude Code uses an **Edit** tool to modify the file
- You'll see a permission prompt asking you to approve the change
- **Read the proposed change before approving it!** This is an important habit.
- After approving, the file is actually modified on disk

### Verify the change

After Claude Code makes the change, run the calculator to test it:

```
Run the calculator.py file to make sure it works
```

Claude Code should use the **Bash** tool to run the file for you. You can also run it yourself in the terminal:

```bash
python3 exercises/02-first-conversation/starter_code/calculator.py
```

## Task 5: Ask for a Bigger Change

Let's try something more ambitious:

```
Modify greeting.py to add a function called personalised_greeting that takes a name and a time of day (morning, afternoon, evening) and returns an appropriate greeting. Add a few examples to the main block.
```

**What to notice:**
- Claude Code generates new code that fits the style of the existing file
- It may create the function and update `__main__` in one or more edits
- The result should be working Python code

**Test it:**

```
Run greeting.py to check the new function works
```

## Task 6: Asking vs Instructing

There's an important difference between **asking questions** and **giving instructions**:

| What You Type | What Happens |
|---------------|-------------|
| "What does this function do?" | Claude Code **explains** — no files change |
| "Add error handling to this function" | Claude Code **modifies files** — you'll see edit proposals |
| "How could I improve this code?" | Claude Code **suggests** — gives advice but doesn't change anything |
| "Improve this code" | Claude Code **acts** — will try to edit the files |

Try both styles and notice the difference:

```
How could the calculate function in calculator.py be improved?
```

Then:

```
Improve the calculate function in calculator.py based on your suggestions
```

## Key Concepts to Remember

| Concept | What It Means |
|---------|--------------|
| **Read tool** | Claude Code reads a file to understand its contents |
| **Edit tool** | Claude Code proposes a change to a file (you must approve it) |
| **Bash tool** | Claude Code runs a command in the terminal |
| **Permission prompts** | Claude Code asks before taking actions — always review before approving |
| **Context** | Claude Code remembers earlier messages in the conversation |

## Check Your Understanding

- How do you open Claude Code in VS Code?
- What's the difference between asking Claude Code a question and giving it an instruction?
- Why is it important to review changes before approving them?
- What tools did Claude Code use during this exercise?

---

**Next up:** [Exercise 3: CLAUDE.md — Teaching Claude About Your Project](../03-claude-md/README.md)
