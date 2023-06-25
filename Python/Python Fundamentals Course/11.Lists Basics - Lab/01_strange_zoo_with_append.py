my_list = []

data = input()
my_list.append(data)

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)
