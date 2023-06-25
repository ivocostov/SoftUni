<<<<<<< HEAD
courses_dictionary = {}

while True:
    command = input()
    if command == 'end':
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses_dictionary.keys():
        courses_dictionary[course_name] = []
    courses_dictionary[course_name].append(student_name)

for course_name, student_names in courses_dictionary.items():
    print(f"{course_name}: {len(student_names)}")
    registered_students = '\n'.join(f"-- {student_names}" for student_names in courses_dictionary[course_name])
    print(registered_students)
=======
courses_dictionary = {}

while True:
    command = input()
    if command == 'end':
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses_dictionary.keys():
        courses_dictionary[course_name] = []
    courses_dictionary[course_name].append(student_name)

for course_name, student_names in courses_dictionary.items():
    print(f"{course_name}: {len(student_names)}")
    registered_students = '\n'.join(f"-- {student_names}" for student_names in courses_dictionary[course_name])
    print(registered_students)
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
