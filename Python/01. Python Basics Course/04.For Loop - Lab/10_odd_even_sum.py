numbers = int(input())

odd_position_nums_sum = 0
even_position_nums_sum = 0

for nums in range(1, numbers + 1):
    current_number = int(input())
    if nums % 2 == 0:
        even_position_nums_sum += current_number
    else:
        odd_position_nums_sum += current_number

if even_position_nums_sum == odd_position_nums_sum:
    print("Yes")
    print(f"Sum = {even_position_nums_sum}")
else:
    difference = abs(even_position_nums_sum - odd_position_nums_sum)
    print("No")
    print(f"Diff = {difference}")

