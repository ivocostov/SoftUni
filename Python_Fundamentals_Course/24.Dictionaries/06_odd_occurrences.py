user_input = input().split()
my_dictionary = {}

for word in user_input:
    word = word.lower()
    if word not in my_dictionary:
        my_dictionary[word] = 0
    my_dictionary[word] += 1

for key, value in my_dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')
