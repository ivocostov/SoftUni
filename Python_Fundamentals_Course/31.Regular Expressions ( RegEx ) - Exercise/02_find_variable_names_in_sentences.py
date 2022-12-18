<<<<<<< HEAD
import re

user_input = input()

pattern = r'\b_([A-Za-z0-9]+)\b'

result = re.findall(pattern, user_input)
=======
import re

user_input = input()

pattern = r'\b_([A-Za-z0-9]+)\b'

result = re.findall(pattern, user_input)
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
print(','.join(result))