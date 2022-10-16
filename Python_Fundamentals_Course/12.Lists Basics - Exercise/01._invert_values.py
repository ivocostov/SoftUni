user_numbers = input().split()

opposite_numbers_list = []

for current_number in user_numbers:
    digits = -int(current_number)
    opposite_numbers_list.append(digits)

print(opposite_numbers_list)
