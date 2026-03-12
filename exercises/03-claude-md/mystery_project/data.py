"""
Data for the grade tracker.
"""

STUDENTS = {
    "Alice Johnson": [85, 92, 78, 90, 88],
    "Bob Smith": [72, 68, 75, 70, 65],
    "Charlie Brown": [95, 98, 92, 97, 100],
    "Diana Ross": [60, 55, 62, 58, 70],
    "Eve Williams": [88, 82, 90, 85, 87],
}

GRADE_BOUNDARIES = {
    90: "HD",   # High Distinction
    80: "D",    # Distinction
    70: "C",    # Credit
    60: "P",    # Pass
    0: "F",     # Fail
}
