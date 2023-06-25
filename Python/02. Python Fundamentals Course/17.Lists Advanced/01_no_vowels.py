user_input = input()

vowels = ['a', 'o', 'u', 'e', 'i']

result = ''.join([letter for letter in user_input if letter.lower() not in vowels])
print(result)
