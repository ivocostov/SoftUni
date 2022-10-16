first_string = input()
second_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]  # [0:character_index + 1 : 1], от началото на стринга до трекущия символ
    right_part = first_string[character_index + 1:]  # [character_index + 1 : len(first_string):1], от текущия символ до края на стринга
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string
