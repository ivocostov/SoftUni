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
