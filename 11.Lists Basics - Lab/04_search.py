number = int(input())
word = input()

all_strings_list = []
word_filtered_list = []

for current_number in range(number):
    current_string = input()
    all_strings_list.append(current_string)

    if word in current_string:
        word_filtered_list.append(current_string)

print(all_strings_list)
print(word_filtered_list)

