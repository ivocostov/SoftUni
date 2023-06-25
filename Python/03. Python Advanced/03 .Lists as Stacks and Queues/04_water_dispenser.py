from collections import deque

water_starting_qty = int(input())
names_deque = deque()

while True:
    name = input()
    if name == 'Start':
        break
    names_deque.append(name)

command = input()
while command != 'End':
    current_command = command.split()
    if current_command[0] == 'refill':
        water_starting_qty += int(current_command[1])
    else:
        for current_name in deque(names_deque):
            if water_starting_qty >= int(current_command[0]):
                print(f"{current_name} got water")
                water_starting_qty -= int(command)
                names_deque.popleft()
                break
            else:
                print(f"{current_name} must wait")
                names_deque.popleft()

    command = input()
print(f"{water_starting_qty} liters left")