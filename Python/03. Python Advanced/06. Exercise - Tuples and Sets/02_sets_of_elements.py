first_set_lenght, second_set_lenght = input().split()

total_sets_lenght = int(first_set_lenght) + int(second_set_lenght)
first_set = set()
second_set = set()

for sequence in range(1, total_sets_lenght + 1):
    number = input()
    if sequence <= int(first_set_lenght):
        first_set.add(number)
    else:
        second_set.add(number)

print(*first_set.intersection(second_set), sep='\n')
