import re

user_input = input()

pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-])+(\.[a-z]+)+)\b'
valid_emails = re.findall(pattern, user_input)

# Emails are in the format "{user}@{host}"
for valid in valid_emails:
    print(valid[0])