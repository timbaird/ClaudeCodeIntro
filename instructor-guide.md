# Instructor Guide

## Pre-Class Preparation

### 1. Repository Setup

Before class, push this repo to GitHub (or your institution's Git hosting) so students can clone it.

```bash
cd claude-code-workshop
git init
git add .
git commit -m "Initial workshop content"
git remote add origin <YOUR_REPO_URL>
git push -u origin main
```

Update `exercises/01-git-basics/README.md` with the actual clone URL.

### 2. Send Pre-Class Instructions

Send students the link to `exercises/00-setup/README.md` **at least a few days before class**. They need to:

1. Install Git
2. Install VS Code
3. Install the Claude Code extension
4. Create an OpenRouter account and get an API key
5. Configure environment variables

**Expect 30-50% of students to not complete pre-class setup.** Budget 15-20 minutes at the start of class for troubleshooting.

### 3. Test the Setup Yourself

Run through the full OpenRouter setup on a clean machine (or at least verify the environment variables and model work). Free models on OpenRouter change frequently — confirm that `qwen/qwen3-coder-480b-a35b-instruct` is still available and free before class.

**Fallback models** (if the recommended one is unavailable):
- `deepseek/deepseek-v3.2-20251201`
- `google/gemini-2.5-flash`
- `openai/gpt-4o-mini`

Check current free models at: [https://openrouter.ai/models?pricing=free](https://openrouter.ai/models?pricing=free)

### 4. Rate Limit Planning

Free OpenRouter models typically allow ~20 requests/minute and ~200 requests/day per account. With 20+ students:

- **Stagger API-heavy exercises**: Exercise 2 (first conversation) will have everyone hitting the API at once. Build in "read and discuss" time between prompts.
- **Have students read before typing**: Each exercise has "What to notice" and explanation sections — encourage students to read these rather than rushing to the next prompt.
- **Prepare for rate limit errors**: Show students what a rate limit error looks like and reassure them it's normal. Wait 30-60 seconds and retry.

---

## Class Schedule

| Time | Exercise | Instructor Notes |
|------|----------|-----------------|
| **0:00 – 0:15** | Setup troubleshooting | Help students who didn't complete pre-class setup. Run `verify_setup.py` together. |
| **0:15 – 0:30** | Exercise 1: Git Basics | Walk through git clone as a group. Most students won't have used Git. |
| **0:30 – 1:00** | Exercise 2: First Conversation | Students work solo. Circulate to help with permission prompts and model issues. |
| **1:00 – 1:30** | Exercise 3: CLAUDE.md | Brief explanation at start, then hands-on. The "before/after" comparison is the key learning moment. |
| *1:30 – 1:45* | *Break* | |
| **1:45 – 2:15** | Exercise 4: Memory & Settings | Mix of demo and hands-on. The settings part is more conceptual. |
| **2:15 – 3:15** | Exercise 5: Build an App | The core exercise. Students should get through at least Steps 1-4. Steps 5-6 are stretch goals. |
| **3:15 – 3:45** | Exercise 6: Advanced Features | More conceptual — demo MCP and agents if possible. Students explore slash commands. |
| **3:45 – 4:00** | Exercise 7: Capstone | Students likely won't finish a full app — that's fine. The goal is to practise the workflow independently. |

---

## Talking Points for Each Exercise

### Exercise 1: Git Basics
- Git is an industry-standard skill — this isn't just for the workshop
- "Clone" = download, "commit" = save a snapshot, "repository" = project folder
- Don't go deep on Git — just enough to clone and understand what's happening

### Exercise 2: First Conversation
- **Key moment**: When students see Claude Code read a file for the first time — point out the tool call
- **Permission prompts**: Explain that Claude Code always asks before taking actions. This is a safety feature, not a bug.
- **Free model issues**: If a student's model gives a strange response, have them try `/clear` and rephrase. Normalise this.

### Exercise 3: CLAUDE.md
- **Key takeaway**: CLAUDE.md is like writing a brief for a new team member
- The before/after comparison is powerful — if students are pressed for time, make sure they at least do Tasks 1-3
- Relate it to real-world practice: professional teams use CLAUDE.md in their repos

### Exercise 4: Memory & Settings
- Memory = personal notes that persist. CLAUDE.md = shared project instructions.
- Don't spend too long on settings.json — the permission modes concept is what matters
- The layered configuration (settings → CLAUDE.md → memory) is the key mental model

### Exercise 5: Build an App
- **This is the centrepiece**. Give it the most time.
- Walk around and help students who get stuck
- Encourage the "prompt, review, approve, test" workflow — don't let students just auto-approve everything
- If a student finishes early, suggest they try the colour or search feature additions
- If a student falls behind, have them skip to the CLI interface (Step 4) and just get something working

### Exercise 6: Advanced Features
- MCP is conceptual for this class — don't worry if students don't set one up
- Agents are also conceptual — the goal is understanding what's happening, not configuring them
- The "Tips and Tricks" section in Part 4 is probably the most practical part — make sure students read it

### Exercise 7: Capstone
- Don't expect finished products — 15 minutes isn't enough
- The goal is practising the **workflow**: CLAUDE.md → build → test → iterate
- Use the reflection questions for class discussion if there's time

---

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Student can't install Git | On macOS, `xcode-select --install` is usually the fix. On Windows, make sure they restart their terminal after installing. |
| Claude Code extension not working | Make sure they installed the one by **Anthropic**, not a third-party one. Try restarting VS Code. |
| "Authentication failed" | Most common cause: `ANTHROPIC_API_KEY` is not set to an empty string. It must be `""`, not unset. |
| Model gives garbage responses | Free model quality varies. Try `/clear` and rephrase. If persistent, try switching models: `/model google/gemini-2.5-flash` |
| "Rate limit exceeded" | Wait 60 seconds. If happening frequently, have the student slow down — read and think between prompts. |
| Student's machine is very slow | OpenRouter is cloud-based so machine speed shouldn't matter for the AI. If VS Code itself is slow, close other applications. |
| Student has paid Claude account | Great! They can skip the OpenRouter setup entirely. Their experience will be better. |
| Student finishes early | Point them to the capstone challenge, or have them help classmates. |
| `verify_setup.py` shows failures | Walk through each failure. Most common: environment variables not loaded (need to restart VS Code). |

---

## About Free vs Paid Models

Throughout the workshop, be upfront:

> "Claude Code is built by Anthropic to work with their Claude models. We're using a free alternative through OpenRouter so nobody needs a paid subscription to participate. The trade-off is that the free model won't be as smooth — it might occasionally misunderstand instructions or produce odd tool calls. That's normal and expected. If you find Claude Code useful and want the full experience, a paid Claude subscription will give significantly better results."

This sets honest expectations without discouraging students. When students hit free model limitations, frame it as "this is where the paid version really shines" rather than "Claude Code is broken."

---

## Assessment Ideas

If you need to assess this workshop:

- **Completion**: Did the student complete exercises 1-5? (Check their modified files)
- **CLAUDE.md quality**: Review the CLAUDE.md they wrote in Exercise 3 — does it cover the key points?
- **Reflection**: Have students submit written answers to the capstone reflection questions
- **Portfolio**: Students keep their capstone project as evidence of using AI-assisted development
- **Practical test**: Give students a new small project and have them use Claude Code to build it (with CLAUDE.md, tests, etc.)
