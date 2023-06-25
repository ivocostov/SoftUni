# JUDGE 50/100

# number_of_students = int(input())
#
# student_info = {}
#
# for _ in range(number_of_students):
#     student, grade = input().split(' ')
#     if student not in student_info.keys():
#         student_info[student] = []
#     student_info[student].append(grade)
#
# for current_student, grades in student_info.items():
#     grades_as_float = [float(num) for num in grades]
#     avg_grade = sum(grades_as_float) / len(grades)
#     print(f"{current_student} -> {' '.join(grades)} (avg: {avg_grade:.2f})")
# ==================================
# JUDGE 100/100

number_of_students = int(input())

student_info = {}

for _ in range(number_of_students):
    student, grade = input().split(' ')
    if student not in student_info.keys():
        student_info[student] = []
    student_info[student].append(float(grade))

for current_student, grades in student_info.items():
    grades_as_str = ' '.join(map(lambda grd: f'{grd:.2f}', grades))
    avg_grade = sum(grades) / len(grades)
    print(f"{current_student} -> {grades_as_str} (avg: {avg_grade:.2f})")
