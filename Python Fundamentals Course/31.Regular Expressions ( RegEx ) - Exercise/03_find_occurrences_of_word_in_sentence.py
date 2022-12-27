<<<<<<< HEAD
import re

sentence = input()
searched_word = input()

pattern = fr'\b{searched_word}\b'
result = re.findall(pattern, sentence, flags=re.IGNORECASE)

print(len(result))
=======
import re

sentence = input()
searched_word = input()

pattern = fr'\b{searched_word}\b'
result = re.findall(pattern, sentence, flags=re.IGNORECASE)

print(len(result))
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
