<<<<<<< HEAD
encrypted_message = input()

message = encrypted_message

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break

    elif command[0] == "ChangeAll":
        letter_to_be_replaced = command[1]
        letter_to_replace = command[2]
        message = message.replace(command[1], command[2])
    elif command[0] == "Insert":
        given_index = int(command[1])
        given_value = command[2]
        message = message[:given_index] + given_value + message[given_index:]
    elif command[0] == "Move":
        letters_to_move = int(command[1])
        message = message[letters_to_move:] + message[:letters_to_move]

print(f"The decrypted message is: {message}")
=======
encrypted_message = input()

message = encrypted_message

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break

    elif command[0] == "ChangeAll":
        letter_to_be_replaced = command[1]
        letter_to_replace = command[2]
        message = message.replace(command[1], command[2])
    elif command[0] == "Insert":
        given_index = int(command[1])
        given_value = command[2]
        message = message[:given_index] + given_value + message[given_index:]
    elif command[0] == "Move":
        letters_to_move = int(command[1])
        message = message[letters_to_move:] + message[:letters_to_move]

print(f"The decrypted message is: {message}")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
