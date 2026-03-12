# Exercise 3: Example CLAUDE.md Solution

This is a reference for instructors — an example of a well-written CLAUDE.md for the mystery project.

---

```markdown
# Student Grade Tracker

A Python command-line application that tracks student grades and generates class reports using the Australian university grading system.

## Project Structure

- `app.py` - Main application: grade calculation, student summaries, and class report generation
- `data.py` - Student data and grade boundary definitions (treat as read-only)
- `utils.py` - Helper functions for formatting and counting pass/fail

## Grading System

Uses Australian university grade boundaries (defined in `data.py`):
- HD (High Distinction): 90+
- D (Distinction): 80-89
- C (Credit): 70-79
- P (Pass): 60-69
- F (Fail): below 60

## Conventions

- snake_case for all functions and variables
- Each function should have a docstring
- Averages are rounded to 1 decimal place
- Grade boundaries must only be defined in data.py (never hardcoded elsewhere)
- Student names are "First Last" format
- Use f-strings for string formatting

## How to Run

```bash
python3 app.py
```

## Important Notes

- Do NOT modify data.py unless adding new students
- New features should go in app.py or utils.py as appropriate
- Keep code simple — this is a teaching project
```
