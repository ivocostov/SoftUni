user_input = list(map(int, input().split(", ")))

even_indexes = map(lambda number: number if user_input[number] % 2 == 0 else 'not', range(len(user_input)))
even_indexes_list = list(filter(lambda index: index != 'not', even_indexes))

print(even_indexes_list)
