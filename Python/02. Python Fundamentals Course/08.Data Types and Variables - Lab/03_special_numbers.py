number = int(input())

for current_number in range(1, number + 1):
    sum_of_digits = 0
    first_digit = current_number % 10
    second_digit = int(current_number / 10)
    sum_of_digits += first_digit + second_digit

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")