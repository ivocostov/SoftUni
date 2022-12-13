import re

text = input()

cool_treshold = 1

for character in text:
    if character.isdigit():
        cool_treshold *= int(character)

pattern = r'(\:\:|\*\*)([A-Z][a-z]{2,})\1'
result = re.findall(pattern, text)

temporary = ''
cool_emojis = []
sum_of_cool_emojis = 0

for emoji in result:
    valid_emoji = str(emoji[-1])
    emoji_symbols = str(emoji[0])
    sum_of_cool_emojis = 0
    temporary = ''

    for character in valid_emoji:
        sum_of_cool_emojis += ord(character)
    if sum_of_cool_emojis > cool_treshold:
        temporary = emoji_symbols + valid_emoji + emoji_symbols
        cool_emojis.append(temporary)

print(f"Cool threshold: {cool_treshold}")
print(f"{len(result)} emojis found in the text. The cool ones are:")
for emoticon in cool_emojis:
    print(emoticon)



# import re
#
# text = input()
#
# pattern = re.compile(r'(?P<all_sum_word>(::|\*\*)(?P<clear_word>[A-Z][a-z]{2,})(\2))')
# digits_pattern = re.compile(r'[0-9]+')
#
# result_text = list(re.finditer(pattern, text))
# result_digits = re.finditer(digits_pattern, text)
#
# list_digits = [x for x in text if x.isdigit()]
# threshold = 1
# for multiply in list_digits:
#     threshold *= int(multiply)
# print(f"Cool threshold: {threshold}")
# print(f"{len(result_text)} emojis found in the text. The cool ones are:")
#
# for result_animal in result_text:
#     ch_sum = 0
#     for ch in result_animal['clear_word']:
#         ch_sum += ord(ch)
#     if ch_sum > threshold:
#         print(f"{result_animal['all_sum_word']}")