word = input()

my_list = []
counter = 0
for i in str(word):
    if i.isupper():
        my_list.append(counter)
    counter += 1
print(my_list)
