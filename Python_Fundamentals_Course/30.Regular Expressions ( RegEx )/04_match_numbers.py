import re

user_input = input()
"""
 Проверява дали преди числото има интервал или е в началото на стринга - positive lookbehind (^|(?<=\s)), 
 дали числото е отрицателно или не -?, дали започва с една цифра или с две, което може да е така и да не е така ([0]|[1-9][0-9]*),
 дали има или няма числа след десетичната запетая (\.\d+)?
 както и дали има интервал преди числото или е в края на стринга - positive lookahead ($|(?=\s))
"""

searched_pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
valid_numbers = re.finditer(searched_pattern, user_input)

for number in valid_numbers:
    print(number.group(), end=' ')
