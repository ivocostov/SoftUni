<<<<<<< HEAD
import re

text = input()

pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)'
result = re.findall(pattern, text)

mirror_words = []
valid_words_counter = 0

for match in result:
    if match[1] == match[3][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[3]}')
    valid_words_counter += 1

if valid_words_counter > 0:
    print(f"{valid_words_counter} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")
=======
import re

text = input()

pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)'
result = re.findall(pattern, text)

mirror_words = []
valid_words_counter = 0

for match in result:
    if match[1] == match[3][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[3]}')
    valid_words_counter += 1

if valid_words_counter > 0:
    print(f"{valid_words_counter} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
