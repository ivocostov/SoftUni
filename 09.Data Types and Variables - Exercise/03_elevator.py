persons = int(input())
elevator_capacity = int(input())

courses_counter = 0
elevator_courses = persons // elevator_capacity
courses_counter += elevator_courses
persons -= elevator_capacity * courses_counter
if persons > 0:
    courses_counter += 1
print(courses_counter)
