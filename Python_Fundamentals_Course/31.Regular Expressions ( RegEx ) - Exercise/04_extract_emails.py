<<<<<<< HEAD
import re

user_input = input()

pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-])+(\.[a-z]+)+)\b'
valid_emails = re.findall(pattern, user_input)

# Emails are in the format "{user}@{host}"
for valid in valid_emails:
=======
import re

user_input = input()

pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-])+(\.[a-z]+)+)\b'
valid_emails = re.findall(pattern, user_input)

# Emails are in the format "{user}@{host}"
for valid in valid_emails:
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
    print(valid[0])