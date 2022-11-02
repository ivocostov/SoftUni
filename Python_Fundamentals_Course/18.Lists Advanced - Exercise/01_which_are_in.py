first_sequence = input().split(", ")
second_sequence = input().split(", ")

new_list = []

for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word:
            if first_word in new_list:
                continue
            new_list.append(first_word)
print(new_list)