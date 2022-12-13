def make_upper(initial_pass, index):
    if index in range(len(initial_pass)):
        initial_pass = initial_pass.replace(initial_pass[index], initial_pass[index].upper())
        print(initial_pass)
    return initial_pass


def make_lower(initial_pass, index):
    if index in range(len(initial_pass)):
        initial_pass = initial_pass.replace(initial_pass[index], initial_pass[index].lower())
        print(initial_pass)
    return initial_pass


def insert(initial_pass, index, char):
    if index in range(len(initial_pass)):
        initial_pass = initial_pass[:index] + char + initial_pass[index:]
        print(initial_pass)
    return initial_pass


def replace(initial_pass, char, value):
    if char in initial_pass:
        ascii_value = ord(char)
        result = chr(ascii_value + value)
        initial_pass = initial_pass.replace(char, result)
        print(initial_pass)
    return initial_pass


def validation(initial_pass):
    upper_letters = ''
    lower_letters = ''
    digits = ''

    if len(initial_pass) < 8:
        print("Password must be at least 8 characters long!")
    if not initial_pass.isalnum():
        print("Password must consist only of letters, digits and _!")
    for character in initial_pass:
        if character.isupper():
            upper_letters += character
        if character.islower():
            lower_letters += character
        if character.isdigit():
            digits += character
    if not upper_letters:
        print("Password must consist at least one uppercase  letter!")

    if not lower_letters:
        print("Password must consist at least one lowercase letter!")

    if not digits:
        print("Password must consist at least one digit!")

    return initial_pass


def main_function(initial_pass):
    while True:
        command = input()
        if command == 'Complete':
            break

        current_command = command.split()
        action = current_command[0]
        if len(current_command) > 1:
            two_words_action = current_command[0] + ' ' + current_command[1]
            if two_words_action == 'Make Upper':
                index = int(current_command[2])
                initial_pass = make_upper(initial_pass, index)
            elif two_words_action == 'Make Lower':
                index = int(current_command[2])
                initial_pass = make_lower(initial_pass, index)

        if action == 'Insert':
            index = int(current_command[1])
            char = current_command[2]
            initial_pass = insert(initial_pass, index, char)
        if action == 'Replace':
            char = current_command[1]
            value = int(current_command[2])
            initial_pass = replace(initial_pass, char, value)
        if action == 'Validation':
            initial_pass = validation(initial_pass)


initial_password = input()
main_function(initial_password)
