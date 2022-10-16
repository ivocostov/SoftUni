number_of_lines = int(input())

char_value_counter = 0

for character in range(1, number_of_lines + 1):
    current_character = input()
    char_value_counter += ord(current_character)
print(f"The sum equals: {char_value_counter}")

