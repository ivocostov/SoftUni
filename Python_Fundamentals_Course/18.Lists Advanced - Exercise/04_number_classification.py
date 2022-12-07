def positive(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative(numbers):
    return [number for number in numbers if int(number) < 0]


def even(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd(numbers):
    return [number for number in numbers if int(number) % 2 != 0]


user_input = input().split(', ')

print(f"Positive: {', '.join(positive(user_input))}")
print(f"Negative: {', '.join(negative(user_input))}")
print(f"Even: {', '.join(even(user_input))}")
print(f"Odd: {', '.join(odd(user_input))}")
