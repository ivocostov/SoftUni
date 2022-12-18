numbers = int(input())
right_sum = 0
left_sum = 0

for nums in range(numbers * 2):
    current_number = int(input())
    if nums < numbers:
        left_sum += current_number
    else:
        right_sum += current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(right_sum - left_sum)
    print(f"No, diff = {difference}")


