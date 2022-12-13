import re

data = input()
pattern = r'F\w'
result = re.findall(pattern, data)
print(result)

"""
Търси съвпадение на думи които започват с F

"""