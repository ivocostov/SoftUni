def key_contains(activation_key, substring):

    if substring in activation_key:
        print(f"{activation_key} contains {substring}")
    else:
        print("Substring not found!")

    return activation_key


def key_flip(activation_key, upper_lower, start_index, end_index):
    if upper_lower == 'Upper':
        activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + activation_key[end_index:]
    elif upper_lower == 'Lower':
        activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]

    print(activation_key)
    return activation_key


def key_slice(activation_key, start_index, end_index):
    activation_key = activation_key[:start_index] + activation_key[end_index:]

    print(activation_key)
    return activation_key


def main_function(activation_key):
    while True:
        command = input()
        if command == 'Generate':
            break

        current_command = command.split('>>>')
        action = current_command[0]

        if action == 'Contains':
            substring = current_command[1]
            activation_key = key_contains(activation_key, substring)
        elif action == 'Flip':
            upper_lower = current_command[1]
            start_index = int(current_command[2])
            end_index = int(current_command[3])
            activation_key = key_flip(activation_key, upper_lower, start_index, end_index)
        elif action == 'Slice':
            start_index = int(current_command[1])
            end_index = int(current_command[2])
            activation_key = key_slice(activation_key, start_index, end_index)

    print(f"Your activation key is: {activation_key}")


raw_activation_key = input()
main_function(raw_activation_key)