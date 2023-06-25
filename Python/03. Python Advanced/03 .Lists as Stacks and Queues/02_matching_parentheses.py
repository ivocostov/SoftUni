user_input = input()

my_stack = []

for index, symbol in enumerate(user_input):
    if symbol == '(':
        my_stack.append(index)
    elif symbol == ')':
        print(user_input[my_stack[-1]:index + 1])
        my_stack.pop()
