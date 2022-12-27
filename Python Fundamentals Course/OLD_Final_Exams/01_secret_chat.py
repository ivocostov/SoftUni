<<<<<<< HEAD
def insert_space(message, index):
    if 0 <= index < len(message):
        message = message[:index] + ' ' + message[index:]
        print(message)
    return message


def reverse(message, substring):
    if substring in message:
        reversed_substring = substring[::-1]
        message = message.replace(substring, '', 1)
        message += reversed_substring
        print(message)
    else:
        print("error")
    return message


def change_all(message, substring, replacement):
    if substring in message:
        message = message.replace(substring, replacement)
        print(message)
    return message


def encrypted_function(message):
    while True:
        command = input().split(":|:")
        if command[0] == "Reveal":
            break

        action = command[0]

        if action == "InsertSpace":
            index = int(command[1])
            message = insert_space(message, index)
        elif action == "Reverse":
            substring = command[1]
            message = reverse(message, substring)
        elif action == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            message = change_all(message, substring, replacement)

    print(f"You have a new text message: {message}")


concealed_message = input()
encrypted_function(concealed_message)
=======
def insert_space(message, index):
    if 0 <= index < len(message):
        message = message[:index] + ' ' + message[index:]
        print(message)
    return message


def reverse(message, substring):
    if substring in message:
        reversed_substring = substring[::-1]
        message = message.replace(substring, '', 1)
        message += reversed_substring
        print(message)
    else:
        print("error")
    return message


def change_all(message, substring, replacement):
    if substring in message:
        message = message.replace(substring, replacement)
        print(message)
    return message


def encrypted_function(message):
    while True:
        command = input().split(":|:")
        if command[0] == "Reveal":
            break

        action = command[0]

        if action == "InsertSpace":
            index = int(command[1])
            message = insert_space(message, index)
        elif action == "Reverse":
            substring = command[1]
            message = reverse(message, substring)
        elif action == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            message = change_all(message, substring, replacement)

    print(f"You have a new text message: {message}")


concealed_message = input()
encrypted_function(concealed_message)
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
