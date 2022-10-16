list_of_numbers = input().split()
count_of_nums_to_remove = int(input())

list_of_numbers_as_digits = []

for number in list_of_numbers:
    list_of_numbers_as_digits.append(int(number))

for first_count in range(1, count_of_nums_to_remove + 1):
    list_of_numbers_as_digits.remove(min(list_of_numbers_as_digits))

print(*list_of_numbers_as_digits, sep=", ")
