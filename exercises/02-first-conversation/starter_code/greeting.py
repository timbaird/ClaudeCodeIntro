"""
A simple greeting program.
This file is used in Exercise 2 to practice talking to Claude Code.
"""


def greet(name):
    return f"Hello, {name}! Welcome to the workshop."


def greet_multiple(names):
    greetings = []
    for name in names:
        greetings.append(greet(name))
    return greetings


def farewell(name):
    return f"Goodbye, {name}! Hope you learned something."


if __name__ == "__main__":
    print(greet("Student"))
    print()

    students = ["Alice", "Bob", "Charlie"]
    for msg in greet_multiple(students):
        print(msg)

    print()
    print(farewell("Student"))
