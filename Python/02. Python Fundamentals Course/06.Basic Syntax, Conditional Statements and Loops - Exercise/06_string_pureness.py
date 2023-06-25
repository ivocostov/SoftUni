strings_count = int(input())

character_1 = ','
character_2 = '.'
character_3 = '_'

for current_string_count in range(strings_count):
    current_string = input()
    if character_1 in current_string or character_2 in current_string or character_3 in current_string:
        print(f"{current_string} is not pure!")
        continue
    print(f"{current_string} is pure.")
