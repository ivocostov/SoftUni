to_do_list = []

while True:
    command = input()
    if command == "End":
        break

    splitted_command = command.split("-")
    priority = int(splitted_command[0])
    task = splitted_command[1]

    to_do_list.append([priority, task])
sorted_tasks = []
for current_task in sorted(to_do_list):
    sorted_tasks.append(current_task[1])

print(sorted_tasks)
