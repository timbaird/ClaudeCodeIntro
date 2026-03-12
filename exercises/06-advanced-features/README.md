# Exercise 6: Advanced Features

**Time: 30 minutes**

## What You'll Learn

- Useful slash commands in Claude Code
- What MCP (Model Context Protocol) servers are
- How Claude Code uses agents and subagents
- Tips and tricks for getting better results

## Part 1: Slash Commands

Claude Code has built-in commands that start with `/`. These are shortcuts for common actions.

### Try These Commands

In the Claude Code chat, try each of these:

| Command | What It Does |
|---------|-------------|
| `/help` | Shows help and available commands |
| `/clear` | Starts a fresh conversation (clears context) |
| `/model` | Shows or changes the current model |
| `/memory` | Shows your memory files |
| `/compact` | Summarises the conversation to save context space |

### Task 1: Explore Slash Commands

```
/help
```

Read through the available commands. Try a few that look interesting.

### Task 2: Use /compact in a Long Conversation

Start a conversation about something (e.g., ask Claude Code to explain several files in the workshop). After several back-and-forth messages, try:

```
/compact
```

This tells Claude Code to summarise the conversation so far into a shorter form. This is useful when your conversation gets very long and Claude Code starts to lose track of earlier context.

**When to use /compact:**
- After completing one task and starting another in the same conversation
- When Claude Code seems to "forget" what you discussed earlier
- When you get a warning about the conversation being too long

---

## Part 2: MCP Servers (Model Context Protocol)

### What is MCP?

MCP is a way to give Claude Code **extra tools** beyond its built-in ones (Read, Edit, Bash, etc.). An MCP server is a small program that provides new capabilities.

Think of it like browser extensions — your browser has built-in features, but extensions add new ones. MCP servers are extensions for Claude Code.

### Examples of What MCP Servers Can Do

| MCP Server | What It Adds |
|------------|-------------|
| **File system** | Advanced file operations |
| **Database** | Query databases directly |
| **Web browser** | Fetch and read web pages |
| **GitHub** | Interact with GitHub (issues, PRs, etc.) |
| **Memory** | Enhanced long-term memory |

### Task 3: See What MCP Servers Are Available

Ask Claude Code:

```
What MCP servers do you currently have access to? List any tools beyond the built-in ones.
```

For a fresh install, there probably won't be any custom MCP servers — that's normal. MCP servers are something you add as you need them.

### How MCP Servers Are Configured

MCP servers are defined in your settings file. Here's what a configuration looks like (you don't need to add this — this is just to show you the format):

```json
{
  "mcpServers": {
    "web-search": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-web-search"],
      "env": {
        "API_KEY": "your-key-here"
      }
    }
  }
}
```

This tells Claude Code: "There's an MCP server called 'web-search' — run it with this command, and it will give you web search capabilities."

### Task 4: Understand the MCP Concept

Ask Claude Code:

```
Explain MCP (Model Context Protocol) to me like I'm a beginner. What problem does it solve and why would I want to use it?
```

The key insight: MCP lets Claude Code interact with **external systems** (databases, APIs, tools) through a standard interface. This makes Claude Code extensible — anyone can write an MCP server to connect Claude Code to anything.

---

## Part 3: Agents and Task Delegation

### What Are Agents?

When Claude Code encounters a complex task, it can spin up **subagents** — smaller, focused workers that handle part of the job. Think of it like a manager delegating tasks:

```
You: "Find all the bugs in this project and fix them"

Claude Code (main agent):
  ├── Subagent 1: Search for error handling issues
  ├── Subagent 2: Look for unused imports
  └── Subagent 3: Check for common Python mistakes
```

Each subagent focuses on one part of the problem and reports back to the main agent.

### Task 5: See Agents in Action

Go back to the workshop root folder and ask Claude Code a complex, multi-part question:

```
Look through all the exercise starter code files in this workshop. For each one, tell me:
1. What the file does
2. If there are any bugs or issues
3. One way each file could be improved
```

**What to notice:**
- Claude Code may use the Task tool to spin up subagents
- Each subagent works on a specific part of the question
- The main agent combines all the results into a single response
- This is faster than doing everything sequentially

### Task 6: Understand When Agents Are Used

Agents are typically used for:
- **Searching across many files** — one agent per section of the codebase
- **Parallel tasks** — doing multiple independent things at once
- **Complex research** — gathering information from different places

You don't control when Claude Code uses agents — it decides automatically. But knowing they exist helps you understand what's happening when Claude Code seems to be doing several things at once.

---

## Part 4: Tips and Tricks

### Getting Better Results

Here are practical tips for working with Claude Code effectively:

#### 1. Be Specific

| Vague (worse results) | Specific (better results) |
|----------------------|--------------------------|
| "Make this better" | "Add input validation to the add_todo function that rejects empty titles" |
| "Fix the bugs" | "The app crashes when I try to complete a task with an ID that doesn't exist. Add error handling for that." |
| "Write some tests" | "Write pytest tests for the TodoManager.add_todo method, covering: adding a normal task, adding a task with an empty title, and checking the auto-increment ID" |

#### 2. Give Context

```
I'm working on the todo app from exercise 5. The app currently crashes when
the user enters a non-numeric value for the task ID. Can you add input
validation to handle this gracefully?
```

#### 3. Use Follow-ups

Don't try to get everything right in one prompt. Have a conversation:

```
You: Add a priority field to tasks
Claude: [makes changes]
You: That looks good, but can you make high priority tasks show first in the list?
Claude: [refines]
You: Perfect. Now add a test for the priority sorting
```

#### 4. When the Model Struggles (Free Tier)

If the free model is giving poor results:
- **Simplify**: Break the task into the smallest possible step
- **Rephrase**: Say the same thing differently
- **Show examples**: "The function should work like this: input X gives output Y"
- **Start fresh**: Use `/clear` and try a new approach
- **Be explicit**: Don't assume the model will infer what you want

#### 5. Use CLAUDE.md Effectively

The most common mistake is not using CLAUDE.md at all. The second most common mistake is making it too long. Keep it focused:
- Project description (2-3 sentences)
- Key files and structure
- Coding conventions
- How to run and test

---

## Part 5: What Else Can Claude Code Do?

Here's a quick overview of other capabilities you might explore on your own:

| Feature | What It Does |
|---------|-------------|
| **Image reading** | Claude Code can look at screenshots and images |
| **Web search** | Can search the web for documentation and answers |
| **Git operations** | Can commit changes, create branches, etc. |
| **Multi-file edits** | Can change multiple files in one go |
| **Jupyter notebooks** | Can read and edit notebook cells |

## Check Your Understanding

- What are three useful slash commands?
- What is an MCP server and what problem does it solve?
- When does Claude Code use subagents?
- What's the difference between a vague prompt and a specific prompt?
- What should you do when the free model is struggling with a request?

---

**Next up:** [Exercise 7: Capstone Challenge](../07-capstone/README.md)
