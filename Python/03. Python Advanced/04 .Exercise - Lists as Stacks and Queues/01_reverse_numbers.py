stack_input = [x for x in input().split()]

new_stack = []

for i in range(len(stack_input)):
    removed_number = stack_input.pop()
    new_stack.append(removed_number)

print(*new_stack, end='')


