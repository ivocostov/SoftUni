def sorted_numbers(input_number):
    list_of_numbers = []
    for current_number in input_number:
        list_of_numbers.append(current_number)
    return sorted(list_of_numbers)


user_input = map(int, input().split())
print(sorted_numbers(user_input))
