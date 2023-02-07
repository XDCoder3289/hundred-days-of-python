student_scores = {
    "Salman": 100,
    "Misha": 10,
    "Hashir": 1,
    "Nomi": 2
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80 and student_scores[key] < 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 70 and student_scores[key] < 80:
        student_grades[key] = "Average"
    elif student_scores[key] < 70:
        student_grades[key] = "Fail"

print(student_grades)