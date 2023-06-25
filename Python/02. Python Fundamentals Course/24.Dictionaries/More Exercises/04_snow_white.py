<<<<<<< HEAD
"""
You will be receiving several input lines which contain data about each dwarf in the following format:
{dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
You must store the data about the dwarfs in your program. There are several rules though:

•	If 2 dwarfs have the same name but different color, they should be considered different dwarfs, and you should
    store them both.
•	If 2 dwarfs have the same name and the same color, store the one with the higher physics.

When you receive the command "Once upon a time", the input ends. You must order the dwarfs by physics in
descending order and then by total count of dwarfs with the same hat color in descending order.
Then you must print them all.
"""

dwarf_dictionary = {}


def show_results():
    # for hat in dwarf_dictionary:
    #     for dwarf_name, dwarf_physic in dwarf_dictionary[hat_color].items():
    #         result_list.append({hat_color: len(dwarf_dictionary[hat_color]), name_d: dwarf_name, physic_d: dwarf_physic, hat_d: hat_color})
    # for show in sorted(result_list, key=lambda item: (-item[physic_d], -item[hat_color])):
    #     print(f"({show[hat_d]}) {show[name_d]} <-> {show[physic_d]}")

    dwarf_physics = []
    for color in dwarf_dictionary.keys():
        for dwarf_name, physic in dwarf_dictionary[color].items():
            dwarf_physics.append([color, dwarf_name, physic])

    #for current_color in dwarf_physics.keys():
    for current_stats in sorted(dwarf_physics, key=lambda item: (item[2], item[len(dwarf_dictionary[hat_color])]), reverse=True):
        print(f"({current_stats[0]}) {current_stats[1]} <-> {current_stats[2]}")


while True:
    initial_input = input()
    if initial_input == 'Once upon a time':
        break

    name, hat_color, physics = [int(x) if x.isdigit() else x for x in initial_input.split(' <:> ')]
    dwarf_dictionary[hat_color] = dwarf_dictionary.get(hat_color, {})
    dwarf_dictionary[hat_color][name] = dwarf_dictionary[hat_color].get(name, 0)
    if dwarf_dictionary[hat_color][name] < physics:
        dwarf_dictionary[hat_color][name] = physics


show_results()
=======
"""
You will be receiving several input lines which contain data about each dwarf in the following format:
{dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
You must store the data about the dwarfs in your program. There are several rules though:

•	If 2 dwarfs have the same name but different color, they should be considered different dwarfs, and you should
    store them both.
•	If 2 dwarfs have the same name and the same color, store the one with the higher physics.

When you receive the command "Once upon a time", the input ends. You must order the dwarfs by physics in
descending order and then by total count of dwarfs with the same hat color in descending order.
Then you must print them all.
"""

dwarf_dictionary = {}


def show_results():
    # for hat in dwarf_dictionary:
    #     for dwarf_name, dwarf_physic in dwarf_dictionary[hat_color].items():
    #         result_list.append({hat_color: len(dwarf_dictionary[hat_color]), name_d: dwarf_name, physic_d: dwarf_physic, hat_d: hat_color})
    # for show in sorted(result_list, key=lambda item: (-item[physic_d], -item[hat_color])):
    #     print(f"({show[hat_d]}) {show[name_d]} <-> {show[physic_d]}")

    dwarf_physics = []
    for color in dwarf_dictionary.keys():
        for dwarf_name, physic in dwarf_dictionary[color].items():
            dwarf_physics.append([color, dwarf_name, physic])

    #for current_color in dwarf_physics.keys():
    for current_stats in sorted(dwarf_physics, key=lambda item: (item[2], item[len(dwarf_dictionary[hat_color])]), reverse=True):
        print(f"({current_stats[0]}) {current_stats[1]} <-> {current_stats[2]}")


while True:
    initial_input = input()
    if initial_input == 'Once upon a time':
        break

    name, hat_color, physics = [int(x) if x.isdigit() else x for x in initial_input.split(' <:> ')]
    dwarf_dictionary[hat_color] = dwarf_dictionary.get(hat_color, {})
    dwarf_dictionary[hat_color][name] = dwarf_dictionary[hat_color].get(name, 0)
    if dwarf_dictionary[hat_color][name] < physics:
        dwarf_dictionary[hat_color][name] = physics


show_results()
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
