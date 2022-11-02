secret_message = input().split()

deciphered_word = []

for word in secret_message:
    numbers_list = ""
    letters_list = []
    for character in word:
        if character.isdigit():
            numbers_list += character
            letter_from_digits = chr(int(numbers_list))
        else:
            letters_list.append(character)

    letters_list[0], letters_list[-1] = letters_list[-1], letters_list[0]
    letters_list.insert(0, letter_from_digits)
    deciphered_word.append(''.join(letters_list))


print(' '.join(deciphered_word))
