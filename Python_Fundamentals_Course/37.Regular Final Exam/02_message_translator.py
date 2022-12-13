import re

number = int(input())



for _ in range(number):
    user_input = input()

    pattern = r'(\!)([A-Z][a-z]{2,})\1(\:)(\[)([A-Za-z]{8,})(\])'
    result = re.findall(pattern, user_input)

    if not result:
        print("The message is invalid")
    else:
        temporary = str(result[0][4])
        digits_list = []
        for character in temporary:
            character_as_digit = ord(character)
            digits_list.append(str(character_as_digit))
        digits = ' '.join(digits_list)
        final_result = f"{result[0][1]}: {digits}"
        print(final_result)
