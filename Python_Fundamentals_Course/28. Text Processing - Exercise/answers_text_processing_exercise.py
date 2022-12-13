# 1

def length_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters_are_valid(name):
    for character in name:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
    return True


def no_redundant_symbols_(name):
    if ' ' in name:
        return False
    return True


def username_validation(name):
    if length_is_valid(name) and characters_are_valid(name) and no_redundant_symbols_(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_validation(username):
        print(username)

# 2

first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else:  # len(first_string) == len(second_string)
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)

# 3

filename_with_extension = input().split("\\")
filename, extension = filename_with_extension[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")

# 4

start_message = input()
final_message = ''
for character in start_message:
    new_symbol = chr(ord(character) + 3)
    final_message += new_symbol
print(final_message)

# 5

single_string = input()
for index in range(len(single_string)):
    if single_string[index] == ":":  # if single_string[index] == ":" and index != len(single_string) - 1:
        print(f":{single_string[index + 1]}")

    # 6

some_text = input()
final_text = ""
last_letter = ""
for current_letter in some_text:
    if current_letter != last_letter:
        final_text += current_letter
        last_letter = current_letter
print(final_text)

# 7

some_text = input()
new_text = ""
strength = 0
for index in range(len(some_text)):
    if strength > 0 and some_text[index] != ">":  # We have to skip/explode current letter
        strength -= 1
    elif some_text[index] == ">":
        new_text += some_text[index]
        strength += int(some_text[index + 1])
    else:
        new_text += some_text[index]
print(new_text)

# 8


data = input().split()
total_sum = 0
for current_string in data:
    current_number = int(current_string[1:len(current_string) - 1])
    first_letter = current_string[0]
    last_letter = current_string[-1]
    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += current_number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += current_number * first_letter_position
    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position
print(f"{total_sum:.2f}")


# 10

def is_winning_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetitions = match_symbol * uninterrupted_match_length
            if winning_symbol_repetitions in left_part and winning_symbol_repetitions in right_part:
                if uninterrupted_match_length == 10:  # We have Jackpot here
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'  # We have just winning ticket
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(is_winning_ticket(ticket))