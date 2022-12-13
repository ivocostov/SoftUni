def memory_game(list_of_digits):
    number_of_moves_until_now = 0

    while True:
        command = input()
        if command == 'end':
            break
        elif len(list_of_digits) == 0:
            print(f"You have won in {number_of_moves_until_now} turns!")
            break
        number_of_moves_until_now += 1

        index1, index2 = list(map(int, command.split()))

        if index1 < 0 or index2 < 0 or index1 > int(len(list_of_digits)) or index2 > int(len(list_of_digits)) or index1 == index2:
            # list_of_digits.insert(int(len(list_of_digits) / 2), f"{-number_of_moves_until_now}a")
            # list_of_digits.insert(int(len(list_of_digits) / 2), f"{-number_of_moves_until_now}a")
            list_of_digits_middle = len(list_of_digits) // 2
            elements_to_add = str(-number_of_moves_until_now) + 'a'
            list_of_digits[list_of_digits_middle:list_of_digits_middle] = [elements_to_add] * 2
            print("Invalid input! Adding additional elements to the board")
            continue

        first_number = list_of_digits[index1]
        second_number = list_of_digits[index2]

        if first_number == second_number:
            print(f"Congrats! You have found matching elements - {first_number}!")
            list_of_digits.remove(first_number)
            list_of_digits.remove(second_number)
        else:
            print("Try again!")
    return list_of_digits


sequence_of_elements = input().split()
memory_game(sequence_of_elements)

if len(sequence_of_elements) > 0:
    print(f"Sorry you lose :(")
    print(' '.join(sequence_of_elements))
