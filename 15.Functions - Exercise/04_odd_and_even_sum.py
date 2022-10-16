def numbers(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for current_number in number:
        if int(current_number) % 2 == 0:
            sum_of_even_digits += int(current_number)
        else:
            sum_of_odd_digits += int(current_number)
    return sum_of_odd_digits, sum_of_even_digits


user_input = input()
sum_of_odd_digits, sum_of_even_digits = numbers(user_input)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
