"""
A simple calculator module.
This file is used in Exercise 2 to practice asking Claude Code questions.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def calculate(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        return f"Error: Unknown operator '{operator}'"


if __name__ == "__main__":
    print("Simple Calculator")
    print("-" * 20)
    print(f"10 + 5 = {calculate(10, '+', 5)}")
    print(f"10 - 5 = {calculate(10, '-', 5)}")
    print(f"10 * 5 = {calculate(10, '*', 5)}")
    print(f"10 / 5 = {calculate(10, '/', 5)}")
    print(f"10 / 0 = {calculate(10, '/', 0)}")
