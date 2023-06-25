first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    even_numbers_sum = 0
    odd_numbers_sum = 0
    current_number_as_string = str(current_number)

    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0: # добавя се там защото нечетните индекси отговарят на позицийте на четните числа                 index: 0 1 2 3
            odd_numbers_sum += int(digit) # а четните индекси отговарят на нечетни числа                                position: t e x t
        else:
            even_numbers_sum += int(digit)
        #print(f"Index = {index} Digit = {number}")
    if even_numbers_sum == odd_numbers_sum:
        print(current_number_as_string, end=" ")

