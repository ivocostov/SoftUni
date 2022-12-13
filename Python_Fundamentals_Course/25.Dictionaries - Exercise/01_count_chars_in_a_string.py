user_text_input = input()

joined_input = user_text_input.replace(" ", "")
my_dictionary = {}

for letter in joined_input:
    if letter not in my_dictionary:
        my_dictionary[letter] = 0
    my_dictionary[letter] += 1

for key, value in my_dictionary.items():
    print(f"{key} -> {value}")
