number = int(input())
word = input()

all_strings_list = []
word_filtered_list = []

for current_number in range(number):
    current_string = input()
    all_strings_list.append(current_string)

print(all_strings_list)

for index in range(len(all_strings_list)-1, -1, -1):
    element = all_strings_list[index]
    if word not in element:
        all_strings_list.remove(element)

print(all_strings_list)

