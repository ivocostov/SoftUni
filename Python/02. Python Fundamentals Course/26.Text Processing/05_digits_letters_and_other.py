<<<<<<< HEAD
user_input = input()

digits, letters, symbols = [], [], []

for character in user_input:
    if character.isdigit():
        digits.append(character)
    elif character.isalpha():
        letters.append(character)
    else:
        symbols.append(character)

print(''.join(digits))
print(''.join(letters))
print(''.join(symbols))
=======
user_input = input()

digits, letters, symbols = [], [], []

for character in user_input:
    if character.isdigit():
        digits.append(character)
    elif character.isalpha():
        letters.append(character)
    else:
        symbols.append(character)

print(''.join(digits))
print(''.join(letters))
print(''.join(symbols))
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
