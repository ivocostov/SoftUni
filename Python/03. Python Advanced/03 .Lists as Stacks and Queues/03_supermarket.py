# clients = []
# name = input()
# while name != 'End':
#     if name != 'Paid':
#         clients.append(name)
#     else:
#         print('\n'.join(clients))
#         clients.clear()
#     name = input()
# print(f"{len(clients)} people remaining.")

# ############################################

from collections import deque

names_deque = deque()
COMMAND_END = 'End'
COMMAND_PAID = 'Paid'

while True:
    command = input()
    if command == COMMAND_END:
        print(f"{len(names_deque)} people remaining.")
    elif command == COMMAND_PAID:
        while names_deque:
            print(names_deque.popleft())
    else:
        names_deque.append(command)
