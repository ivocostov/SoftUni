students_dictionary = {}

number_of_pairs = int(input())

for pairs in range(number_of_pairs):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_dictionary:
        students_dictionary[student_name] = []
    students_dictionary[student_name].append(student_grade)

for name, grade in students_dictionary.items():
    average_grade = sum(students_dictionary[name]) / len(students_dictionary[name])
    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")
    continue
