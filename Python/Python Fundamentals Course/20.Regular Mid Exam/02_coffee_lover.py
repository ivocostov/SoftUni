def include(list_of_coffees, name_of_coffee):
    list_of_coffees.append(name_of_coffee)
    return list_of_coffees


def remove(list_of_coffees, command, count):
    if int(count) > len(list_of_coffees):
        if command == "first":
            del list_of_coffees[:int(count)]
        elif command == "last":
            del list_of_coffees[-int(count):]
    return list_of_coffees


def prefer(list_of_coffees, first_index, second_index):
    first_index_as_digit = int(first_index)
    second_index_as_digit = int(second_index)
    if 0 < first_index_as_digit < len(list_of_coffees) and 0 < second_index_as_digit < len(list_of_coffees):
        list_of_coffees[int(first_index)], list_of_coffees[int(second_index)] = list_of_coffees[int(second_index)], list_of_coffees[int(first_index)]
    return list_of_coffees


def reverse(list_of_coffees):
    list_of_coffees.reverse()
    return list_of_coffees


def coffee_lover(list_of_coffees, commands_count):
    for current_command in range(1, commands_count + 1):

        user_command = input()
        current_cmd, second_condition = user_command.split()

        if current_command == "Include":
            list_of_coffees = include(list_of_coffees, second_condition)
        elif current_command == "Remove":
            additional_1, additional_2 = second_condition.split()
            list_of_coffees = remove(list_of_coffees, additional_1, additional_2)
        elif current_command == "Prefer":
            coffee_index_1, coffee_index_2 = second_condition.split()
            list_of_coffees = prefer(list_of_coffees, coffee_index_1, coffee_index_2)
        elif current_command == "Reverse":
            list_of_coffees = reverse(list_of_coffees)

    final_list = ' '.join(list_of_coffees)

    print(f"Coffees:\n{final_list}")


names_of_coffees = input().split()
number_of_commands = int(input())
if number_of_commands not in range(1, 101):
    exit()
coffee_lover(names_of_coffees, number_of_commands)
