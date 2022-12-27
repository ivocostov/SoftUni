def even_numbers(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False


user_input = input().split()

result = filter(even_numbers, user_input)

even_numbers_list = []

for number in result:
    even_numbers_list.append(int(number))

print(even_numbers_list)

