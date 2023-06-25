# user_string = input()
#
# result = ''
# for letter in user_string[::-1]:
#     result += letter
# print(result)


my_stack = list(input())

while my_stack:
    element = my_stack.pop()
    print(element, end='')