final_string = ''

while True:
    command = input()
    if command == 'End':
        break

    current_command = command.split()

    if current_command[0] == 'Add':
        final_string += current_command[1]

    elif current_command[0] == 'Upgrade':
        given_char = current_command[1]
        target_char = chr(ord(current_command[1]) + 1)
        for symbol in final_string:
            final_string = final_string.replace(given_char, target_char)

    elif current_command[0] == 'Print':
        print(final_string)

    elif current_command[0] == 'Index':
        letter = current_command[1]
        if letter not in final_string:
            print('None')
        else:
            #searched_index = int(final_string.index(letter))
            indices_list = []
            for current_letter in final_string:
                if current_letter == letter:
                    indices_list.append(final_string.index(current_letter))

            print(' '.join(map(str, indices_list)))
    elif current_command[0] == 'Remove':
        substring = current_command[1]
        if substring in final_string:
            final_string = final_string.replace(substring, '')

