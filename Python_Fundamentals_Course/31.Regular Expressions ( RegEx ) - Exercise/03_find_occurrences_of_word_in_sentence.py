import re

sentence = input()
searched_word = input()

pattern = fr'\b{searched_word}\b'
result = re.findall(pattern, sentence, flags=re.IGNORECASE)

print(len(result))
