def absolute_values():
    user_numbers = input().split()
    numbers = []

    for current_number in user_numbers:
        numbers.append(abs(float(current_number)))

    print(numbers)


absolute_values()
