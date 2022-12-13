to_remove_input = input()
user_string = input()

while to_remove_input in user_string:
    user_string = user_string.replace(to_remove_input, "")

print(user_string)
