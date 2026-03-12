"""
Mystery Project - A student grade tracker.
Students will figure out what this does and write a CLAUDE.md for it.
"""

from data import STUDENTS, GRADE_BOUNDARIES


def calc_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def get_letter_grade(score):
    for boundary, grade in sorted(GRADE_BOUNDARIES.items(), reverse=True):
        if score >= boundary:
            return grade
    return "F"


def get_student_summary(student_name):
    if student_name not in STUDENTS:
        return None

    scores = STUDENTS[student_name]
    avg = calc_average(scores)
    grade = get_letter_grade(avg)

    return {
        "name": student_name,
        "scores": scores,
        "average": round(avg, 1),
        "grade": grade,
        "highest": max(scores),
        "lowest": min(scores),
    }


def get_class_report():
    report = []
    for name in sorted(STUDENTS.keys()):
        summary = get_student_summary(name)
        report.append(summary)
    return report


def print_report():
    print("=" * 50)
    print("CLASS REPORT")
    print("=" * 50)

    report = get_class_report()
    for student in report:
        print(f"\n{student['name']}:")
        print(f"  Scores: {student['scores']}")
        print(f"  Average: {student['average']}")
        print(f"  Grade: {student['grade']}")
        print(f"  Range: {student['lowest']} - {student['highest']}")

    averages = [s["average"] for s in report]
    class_avg = calc_average(averages)
    print(f"\n{'=' * 50}")
    print(f"Class Average: {round(class_avg, 1)}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    print_report()
