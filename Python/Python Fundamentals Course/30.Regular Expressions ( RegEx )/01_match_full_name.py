<<<<<<< HEAD
import re

user_input = input()

search_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
valid_name = re.findall(search_pattern, user_input)

print(' '.join(valid_name))
=======
import re

user_input = input()

search_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
valid_name = re.findall(search_pattern, user_input)

print(' '.join(valid_name))
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
