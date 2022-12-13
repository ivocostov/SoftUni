import re

user_input = input()

search_pattern = r'\+359\s2\s\d{3}\s\d{4}\b|\+359\-2-\d{3}\-\d{4}\b'
valid_phone_numbers = re.findall(search_pattern, user_input)

print(', '.join(valid_phone_numbers))