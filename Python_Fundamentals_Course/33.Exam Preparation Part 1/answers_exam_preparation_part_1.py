#   fancy barcodes

import re

number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    barcode = input()
    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
    result = re.match(pattern, barcode)

    if not result:
        print('Invalid barcode')
    else:
        extract_nums = re.findall('\d', result.group())

        if not extract_nums:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(extract_nums)}")


# The pianist

def store_data_func(number):
    data = {}
    for _ in range(number):
        current_data = input().split('|')
        piece = current_data[0]
        composer = current_data[1]
        key = current_data[2]

        data[piece] = [composer, key]

    return data


def add_command_function(piece, composer, key, data):
    if piece not in data:
        data[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_function(piece, data):
    if piece in data:
        print(f"Successfully removed {piece}!")
        del data[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_function(piece, new_key, data):
    if piece in data:
        # Our dictionary for example ---> {'Fur Elise': ['Beethoven', 'A Minor']}
        # At the index 0 in list is composer, at the index 1 is a specific key
        data[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_function(data):
    result = ''
    for piece in data:
        composer = data[piece][0]
        key = data[piece][1]
        result += f"{piece} -> Composer: {composer}, Key: {key}\n"

    return result


# Our core function that navigates our entire program. Each time in it
# we will accept one element as a parameter -- > number of pieces
def the_pianist_func(number):
    # store_data_func returns a dictionary containing as key the name of
    # pieces and as value containing a list of two elements. At index 0 in
    # the list is the name of composer, and at the index 1 in the list is
    # specific key
    data = store_data_func(number)

    while True:
        command = input().split('|')

        if command[0] == 'Stop':
            print(print_function(data))
            break

        current_command = command[0]
        piece = command[1]

        if current_command == 'Add':
            composer = command[2]
            key = command[3]
            add_command_function(piece, composer, key, data)

        elif current_command == 'Remove':
            remove_function(piece, data)

        elif current_command == 'ChangeKey':
            new_key = command[2]
            change_key_function(piece, new_key, data)


number_of_pieces = int(input())
the_pianist_func(number_of_pieces)

# destination mapper
import re

data = input()
pattern = r'(=|\/)[A-Z][A-Za-z]{2,}\1'
result = re.finditer(pattern, data)

points = 0
all_destinations = []

for destination in result:
    current_destination = re.split('\/|=', destination.group())[1]
    points += len(current_destination)
    all_destinations.append(current_destination)

print(f"Destinations: {', '.join(all_destinations)}")
print(f"Travel Points: {points}")

# secret chat

data = input()

while True:

    command = input().split(':|:')
    current_command = command[0]

    if current_command == 'Reveal':
        print(f"You have a new text message: {data}")
        break

    elif current_command == 'InsertSpace':
        index = int(command[1])
        data = data[:index] + ' ' + data[index:]
        print(data)

    elif current_command == 'Reverse':
        substring = command[1]
        if substring in data:
            data = data.replace(substring, '', 1)
            data = data + substring[::-1]
            print(data)
        else:
            print('error')

    elif current_command == 'ChangeAll':
        substring, replacement = command[1], command[2]
        data = data.replace(substring, replacement)
        print(data)