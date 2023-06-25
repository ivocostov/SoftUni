# 1


first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []
for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word:
            substrings.append(first_word)
            break
print(substrings)

# 1.1


first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]
print(substrings)

# 2

version = [int(number) for number in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1
print('.'.join(str(number) for number in version))

# 3

words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print('\n'.join(filtered_words))


# 4

def positive_numbers(some_numbers):
    return [number for number in some_numbers if int(number) >= 0]


def negative_numbers(some_numbers):
    return [number for number in some_numbers if int(number) < 0]


def odd_numbers(some_numbers):
    return [number for number in some_numbers if int(number) % 2 != 0]


def even_numbers(some_numbers):
    return [number for number in some_numbers if int(number) % 2 == 0]


numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")


# 5

def check_the_rooms(numbers_of_rooms):
    total_free_chairs = 0
    total_needed_chairs = 0
    for room in range(1, numbers_of_rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            total_needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {room}")
    return total_free_chairs, total_needed_chairs


number_of_rooms = int(input())
free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")


# 11

def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson(list_of_lessons, title, index):
    if title not in list_of_lessons:
        list_of_lessons.insert(index, title)
    return list_of_lessons


def remove_lesson(list_of_lessons, title):
    if title in list_of_lessons:
        title_index = list_of_lessons.index(title)
        if title_index + 1 in range(len(list_of_lessons)):
            if "Exercise" in list_of_lessons[title_index + 1]:
                list_of_lessons.pop(title_index + 1)
        list_of_lessons.remove(title)
    return list_of_lessons


def swap_lessons(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_position + 1 in range(len(list_of_lessons)):
            first_has_exercise = "Exercise" in list_of_lessons[first_position + 1]
        if second_position + 1 in range(len(list_of_lessons)):
            second_has_exercise = "Exercise" in list_of_lessons[second_position + 1]
        list_of_lessons[first_position], list_of_lessons[second_position] = \
            list_of_lessons[second_position], list_of_lessons[first_position]
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_position + 1], list_of_lessons[second_position + 1] = \
                list_of_lessons[second_position + 1], list_of_lessons[first_position + 1]
        elif not first_has_exercise and second_has_exercise:
            list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_position + 1, list_of_lessons.pop(first_position + 1))
    return list_of_lessons


def exercise(list_of_lessons, title):
    if title in list_of_lessons and f"{title}-Exercise" not in list_of_lessons:
        lesson_index = list_of_lessons.index(title)
        list_of_lessons.insert(lesson_index + 1, f"{title}-Exercise")
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(f"{title}-Exercise")
    return list_of_lessons


lessons = input().split(", ")
command = input().split(":")
while len(command) > 1:  # while command[0] != "course start"
    action = command[0]
    lesson_title = command[1]
    if len(command) > 2:
        lesson_title_or_index = command[2]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(lesson_title_or_index))
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        lessons = swap_lessons(lessons, lesson_title, lesson_title_or_index)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input().split(":")
for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")