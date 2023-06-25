<<<<<<< HEAD
import re

user_input = input()

searched_pattern = r'\d+'

while user_input:
    result = re.findall(searched_pattern, user_input)
    if result:
        print(' '.join(result), end=' ')
    user_input = input()
=======
import re

user_input = input()

searched_pattern = r'\d+'

while user_input:
    result = re.findall(searched_pattern, user_input)
    if result:
        print(' '.join(result), end=' ')
    user_input = input()
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
