number = int(input())

numbers_list = []
filtered_numbers_list = []

for num in range(number):
    current_command = int(input())
    numbers_list.append(current_command)

current_command = input()

if current_command == 'even':
    for current_number in numbers_list:
        if current_number % 2 == 0:
            filtered_numbers_list.append(current_number)
if current_command == 'odd':
    for current_number in numbers_list:
        if current_number % 2 != 0:
            filtered_numbers_list.append(current_number)
if current_command == 'negative':
    for current_number in numbers_list:
        if current_number < 0:
            filtered_numbers_list.append(current_number)
if current_command == 'positive':
    for current_number in numbers_list:
        if current_number >= 0:
            filtered_numbers_list.append(current_number)
print(filtered_numbers_list)
