number = int(input())

# constant values
command_even = 'even'
command_odd = 'odd'
command_positive = 'positive'
command_negative = 'negative'

numbers_list = []
# accepting numbers from user input
for _ in range(number):
    current_number = int(input())
    numbers_list.append(current_number)

command = input()

filtered_numbers = []
# cycling numbers in numbers_list
for number in numbers_list:
    filtered_passes = (
        (command == command_even and number % 2 == 0)
        or (command == command_odd and number % 2 != 0)
        or (command == command_negative and number < 0)
        or (command == command_positive and number >= 0)
    )
    if filtered_passes:
        filtered_numbers.append(number)
print(filtered_numbers)
