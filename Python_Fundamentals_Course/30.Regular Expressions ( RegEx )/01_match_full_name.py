import re

user_input = input()

search_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
valid_name = re.findall(search_pattern, user_input)

print(' '.join(valid_name))
