user_input = input().split(", ")

dictionary = {key: ord(key) for key in user_input}
print(dictionary)
