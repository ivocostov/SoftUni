from collections import deque


def best_list_pureness(*args):
    numbers = args[0]
    rotation_number = args[-1]
    rotations = 0
    list_of_numbers = deque()
    operation_results = {}

    for num in numbers:
        list_of_numbers.append(num)

    for rotation in range(rotation_number):
        current_operation_result = 0
        for index, number in enumerate(list_of_numbers):
            multiplication_result = index * number
            current_operation_result += multiplication_result
        operation_results[rotations] = current_operation_result
        rotations += 1
        list_of_numbers.appendleft(list_of_numbers.pop())

    max_pureness = max(operation_results.values())

    for key, value in operation_results.items():
        if value == max_pureness:
            return f"Best pureness {value} after {key} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)

