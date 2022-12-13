initial_number = int(input())
pianists_dict = {}

for initial in range(initial_number):
    command = input()
    piece, composer, key = command.split("|")
    pianists_dict[piece] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        break
    splitted_command = command.split("|")
    given_command = splitted_command[0]

    if given_command == "Add":
        piece = splitted_command[1]
        composer = splitted_command[2]
        key = splitted_command[3]
        if piece in pianists_dict.keys():
            print(f"{piece} is already in the collection!")
        else:
            pianists_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif given_command == "Remove":
        piece = splitted_command[1]
        if piece in pianists_dict.keys():
            del pianists_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif given_command == "ChangeKey":
        piece = splitted_command[1]
        new_key = splitted_command[2]
        if piece in pianists_dict.keys():
            pianists_dict[piece].append(new_key)
            pianists_dict[piece].pop(1)
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, values in pianists_dict.items():
    print(f"{piece} -> Composer: {values[0]}, Key: {values[1]}")
