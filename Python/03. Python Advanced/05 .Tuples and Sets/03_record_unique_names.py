number_of_inputs = int(input())

list_of_names = set()

for current_name in range(number_of_inputs):
    name = input()
    if name not in list_of_names:
        list_of_names.add(name)

print(*list_of_names, sep='\n')