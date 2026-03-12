"""
Utility functions for the grade tracker.
"""


def format_percentage(value):
    return f"{value:.1f}%"


def format_score_list(scores):
    return ", ".join(str(s) for s in scores)


def is_passing(average):
    return average >= 60


def count_passing(report):
    return sum(1 for student in report if is_passing(student["average"]))


def count_failing(report):
    return sum(1 for student in report if not is_passing(student["average"]))
