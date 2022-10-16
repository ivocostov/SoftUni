def round_numbers(numbers):
    rounded_numbers = []
    for number in numbers:
        current_number = float(number)
        result = round(current_number)
        rounded_numbers.append(result)
    return rounded_numbers


input_numbers = input().split()
print(round_numbers(input_numbers))
