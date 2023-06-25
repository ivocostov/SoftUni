number_of_inputs = int(input())

stack = []

PUSH = '1'
DELETE = '2'
MAX_NUMBER = '3'
MIN_NUMBER = '4'

for _ in range(number_of_inputs):
    command = input()
    if command.startswith(PUSH):
        current_command = command.split()
        stack.append(int(current_command[1]))
    elif command == DELETE:
        if stack:
            stack.pop()
        else:
            continue
    elif command == MAX_NUMBER:
        print(max(stack))
    elif command == MIN_NUMBER:
        print(min(stack))

print(*stack[::-1], sep=', ')
