student_name = input()
sum_of_grades = 0
years_of_study = 0
fails_counter = 0

while True:
    annual_grade = float(input())
    years_of_study += 1
    if annual_grade >= 4:
        sum_of_grades += annual_grade
    if annual_grade < 4:
        fails_counter += 1
        if fails_counter == 2:
            print(f"{student_name} has been excluded at {years_of_study} grade")
            break
        years_of_study -= 1
    if years_of_study == 12:
        average_grade = sum_of_grades / 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break



