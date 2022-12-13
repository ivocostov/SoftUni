user_input = list(map(int, input().split()))

average_value = sum(user_input) / len(user_input)

numbers_above_average = [num for num in sorted(user_input, reverse=True) if num > average_value]

if len(numbers_above_average) != 0:
    print(' '.join(map(str, numbers_above_average[:5])))
else:
    print("No")
