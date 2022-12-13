import re

user_input = input()

pattern = r'\b_([A-Za-z0-9]+)\b'

result = re.findall(pattern, user_input)
print(','.join(result))