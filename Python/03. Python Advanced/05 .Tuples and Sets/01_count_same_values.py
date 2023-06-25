numbers = tuple(map(float, input().split()))

numbers_dict = {}

for num in numbers:
    if num not in numbers_dict:
        numbers_dict[num] = 1
    else:
        numbers_dict[num] += 1
[print(f"{key} - {value} times") for key, value in numbers_dict.items()]
