student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
grade = ""
for student, score in student_scores.items():
    if 90 < score <= 100:
        grade = "Outstanding"
    elif 80 < score <= 90:
        grade = "Exceeds Expectations"
    elif 70 < score <= 80:
        grade = "Acceptable"
    elif 0 < score <= 70:
        grade = "Fail"
    student_grades[student] = grade
print(student_grades)