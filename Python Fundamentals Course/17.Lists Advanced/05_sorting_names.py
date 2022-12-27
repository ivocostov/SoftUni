user_input = input().split(', ')

'''новият лист сортира имената по дължина (от най-дългото към най-късото "-len()", ако се използва "len()" ще ги сортира от най-късото към най-дългото.
", name" в края на реда ги сортира по азбучен ред)'''

sorted_names_list = sorted(user_input, key=lambda name: (-len(name), name))
print(sorted_names_list)
