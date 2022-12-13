def takeodd_function(user_string):
    new_valid_password = ''
    for index in range(1, len(user_string)):
        if int(index) % 2 != 0:
            new_valid_password += user_string[index]
    print(new_valid_password)
    return new_valid_password


def cut_function(user_string, index, lenght):
    user_string = user_string[:index] + user_string[index + lenght:]
    print(user_string)
    return user_string


def substitute_function(user_string, substring, substitute):
    if substring in user_string:
        user_string = user_string.replace(substring, substitute)
        print(user_string)
    else:
        print("Nothing to replace!")

    return user_string


def password_reset(user_string):
    while True:
        command = input().split()
        if command[0] == "Done":
            break

        action = command[0]
        if action == 'TakeOdd':
            user_string = takeodd_function(user_string)
        elif action == 'Cut':
            index = int(command[1])
            lenght = int(command[2])
            user_string = cut_function(user_string, index, lenght)
        elif action == 'Substitute':
            substring = command[1]
            substitute = command[2]
            user_string = substitute_function(user_string, substring, substitute)

    print(f"Your password is: {user_string}")


text = input()
password_reset(text)
