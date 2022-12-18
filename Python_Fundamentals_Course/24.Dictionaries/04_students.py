<<<<<<< HEAD
students = {}

user_input = input().split(":")
while len(user_input) > 1:

    name, id, course = user_input[0], user_input[1], user_input[2]

    if course not in students.keys():
        students[course] = []
    students[course].append(f"{name} - {id}")
    user_input = input().split(":")

searched_course = user_input[0].replace("_", " ")
for current_course in students[searched_course]:
    print(current_course)
=======
students = {}

user_input = input().split(":")
while len(user_input) > 1:

    name, id, course = user_input[0], user_input[1], user_input[2]

    if course not in students.keys():
        students[course] = []
    students[course].append(f"{name} - {id}")
    user_input = input().split(":")

searched_course = user_input[0].replace("_", " ")
for current_course in students[searched_course]:
    print(current_course)
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
