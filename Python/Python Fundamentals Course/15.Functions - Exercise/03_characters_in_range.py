def ascii_characters(char_1, char_2):
    in_between_characters_list = []

    for character in range(ord(char_1) + 1, ord(char_2)):
        current_character = chr(character)
        in_between_characters_list.append(current_character)

    return in_between_characters_list


character_1 = input()
character_2 = input()
print(' '.join(ascii_characters(character_1, character_2)))
