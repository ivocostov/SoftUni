from math import ceil
employee_1_efficiency_per_hour = int(input())
employee_2_efficiency_per_hour = int(input())
employee_3_efficiency_per_hour = int(input())
students_count = int(input())

total_employees_efficiency_per_hour = employee_1_efficiency_per_hour + employee_2_efficiency_per_hour \
                                      + employee_3_efficiency_per_hour
total_time_to_answer_qst = 0
#avg_time_needed_to_answer_qst = ceil(students_count / total_employees_efficiency_per_hour)

for hours in range(1, students_count + 1):
    students_count -= total_employees_efficiency_per_hour
    if hours % 4 == 0:
        total_time_to_answer_qst += 1
        continue
    if students_count < 0:
        break
    total_time_to_answer_qst += 1


print(f"Time needed: {total_time_to_answer_qst}h.")
