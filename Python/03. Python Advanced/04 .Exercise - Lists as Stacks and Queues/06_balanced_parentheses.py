from collections import deque

sequence_of_parentheses = deque(input())
opening_parenthesis = deque()

if len(sequence_of_parentheses) % 2 == 0:
    while sequence_of_parentheses:
        left_sided_parenthesis = sequence_of_parentheses.popleft()

        if left_sided_parenthesis in '([{':
            opening_parenthesis.append(left_sided_parenthesis)

        elif f"{opening_parenthesis.pop() + left_sided_parenthesis}" not in "(){}[]":
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')