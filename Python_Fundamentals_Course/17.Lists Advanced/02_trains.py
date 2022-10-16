number_of_wagons = int(input())
wagons = [0] * number_of_wagons

while True:
    command = input()
    if command == "End":
        break

    splited_command = command.split()
    current_command = splited_command[0]

    if current_command == "add":
        wagons[-1] += int(splited_command[1])
    elif current_command == "insert":
        index_of_wagon = int(splited_command[1])
        ppl_to_be_boarded = splited_command[2]
        wagons[index_of_wagon] += int(ppl_to_be_boarded)
    elif current_command == "leave":
        index_of_wagon = int(splited_command[1])
        ppl_to_leave = splited_command[2]
        wagons[index_of_wagon] -= int(ppl_to_leave)

print(wagons)
