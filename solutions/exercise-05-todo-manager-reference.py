"""
Exercise 5: Reference Solution — TodoManager

This is an INSTRUCTOR REFERENCE ONLY. Students should build their own
version with Claude Code's help. Every student's version will be slightly
different, and that's fine.

This shows what a reasonable completed version looks like.
"""

import json
import os
from datetime import datetime


class TodoManager:
    """Manages a list of todo items with JSON file persistence."""

    def __init__(self, filepath: str = "todos.json"):
        """Initialise the manager with a path to the JSON storage file."""
        self.filepath = filepath
        self.todos = []
        self.next_id = 1
        self.load()

    def load(self):
        """Load todos from the JSON file if it exists."""
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.todos = data.get("todos", [])
                self.next_id = data.get("next_id", 1)

    def save(self):
        """Save todos to the JSON file."""
        data = {
            "todos": self.todos,
            "next_id": self.next_id,
        }
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def add_todo(self, title: str) -> dict:
        """Add a new todo item and return it."""
        if not title.strip():
            raise ValueError("Todo title cannot be empty")

        todo = {
            "id": self.next_id,
            "title": title.strip(),
            "status": "pending",
            "created": datetime.now().isoformat(),
        }
        self.todos.append(todo)
        self.next_id += 1
        self.save()
        return todo

    def list_todos(self, status_filter: str = None) -> list:
        """Return all todos, optionally filtered by status."""
        if status_filter:
            return [t for t in self.todos if t["status"] == status_filter]
        return self.todos

    def complete_todo(self, todo_id: int) -> dict:
        """Mark a todo as complete by ID. Returns the updated todo."""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["status"] = "complete"
                self.save()
                return todo
        raise ValueError(f"No todo found with ID {todo_id}")

    def delete_todo(self, todo_id: int) -> dict:
        """Delete a todo by ID. Returns the deleted todo."""
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                deleted = self.todos.pop(i)
                self.save()
                return deleted
        raise ValueError(f"No todo found with ID {todo_id}")

    def search_todos(self, keyword: str) -> list:
        """Search todos by keyword in title (case-insensitive)."""
        keyword_lower = keyword.lower()
        return [t for t in self.todos if keyword_lower in t["title"].lower()]
