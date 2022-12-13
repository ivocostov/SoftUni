number_of_strings = int(input())

names_list = ''
age_list = ''
letter_start_index = 0
letter_end_index = 0
age_start_index = 0
age_end_index = 0

for _ in range(number_of_strings):
    current_string = input()
    for symbol in current_string:
        if symbol == '@':
            letter_start_index = int(current_string.index(symbol))
        elif symbol == '|':
            letter_end_index = int(current_string.index(symbol))
        elif symbol == '#':
            age_start_index = int(current_string.index(symbol))
        elif symbol == '*':
            age_end_index = int(current_string.index(symbol))

    names_list = current_string[letter_start_index + 1: letter_end_index]
    age_list = current_string[age_start_index + 1: age_end_index]

    print(f"{names_list} is {age_list} years old.")
