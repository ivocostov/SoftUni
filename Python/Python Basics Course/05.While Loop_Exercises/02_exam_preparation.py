bad_grades_qty = int(input())

current_bad_grades = 0
tasks_counter = 0
grades_sum = 0
current_task = input()
last_task = current_task

while current_task != 'Enough':
    tasks_counter += 1
    task_grade = int(input())
    last_task = current_task

    if task_grade <= 4:
        current_bad_grades += 1
    if current_bad_grades == bad_grades_qty:
        print(f"You need a break, {current_bad_grades} poor grades.")
        break

    grades_sum += task_grade
    current_task = input()

if current_task == 'Enough':
    average_grade = grades_sum / tasks_counter
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {tasks_counter}")
    print(f"Last problem: {last_task}")
