<<<<<<< HEAD
def add_stop(tour_stops, given_index, given_string):
    if 0 <= given_index < len(tour_stops):
        tour_stops = tour_stops[:given_index] + given_string + tour_stops[given_index:]
        print(tour_stops)
    return tour_stops


def remove_stop(tour_stops, index_1, index_2):
    if 0 <= index_1 <= index_2 < len(tour_stops):
        tour_stops = tour_stops[:index_1] + tour_stops[index_2 + 1:]
        print(tour_stops)
    else:
        print(tour_stops)
    return tour_stops


def switch(tour_stops, string_1, string_2):
    if string_1 in tour_stops:
        tour_stops = tour_stops.replace(string_1, string_2)
        print(tour_stops)
    # else:                      # на упражненията от 25.11.2022 това го няма
    #     print(tour_stops)
    return tour_stops



def world_tour(world_tour_stops):

    while True:
        command = input()
        if command == "Travel":
            print(f"Ready for world tour! Planned stops: {world_tour_stops}")
            break
        current_command = command.split(":")


        if current_command[0] == "Add Stop":
            current_index = int(current_command[1])
            current_string = current_command[2]
            world_tour_stops = add_stop(world_tour_stops, current_index, current_string)
        elif current_command[0] == "Remove Stop":
            start_index = int(current_command[1])
            end_index = int(current_command[2])
            world_tour_stops = remove_stop(world_tour_stops, start_index, end_index)
        elif current_command[0] == "Switch":
            old_string = current_command[1]
            new_string = current_command[2]
            world_tour_stops = switch(world_tour_stops, old_string, new_string)



tour_stops = input()
world_tour(tour_stops)
=======
def add_stop(tour_stops, given_index, given_string):
    if 0 <= given_index < len(tour_stops):
        tour_stops = tour_stops[:given_index] + given_string + tour_stops[given_index:]
        print(tour_stops)
    return tour_stops


def remove_stop(tour_stops, index_1, index_2):
    if 0 <= index_1 <= index_2 < len(tour_stops):
        tour_stops = tour_stops[:index_1] + tour_stops[index_2 + 1:]
        print(tour_stops)
    else:
        print(tour_stops)
    return tour_stops


def switch(tour_stops, string_1, string_2):
    if string_1 in tour_stops:
        tour_stops = tour_stops.replace(string_1, string_2)
        print(tour_stops)
    # else:                      # на упражненията от 25.11.2022 това го няма
    #     print(tour_stops)
    return tour_stops



def world_tour(world_tour_stops):

    while True:
        command = input()
        if command == "Travel":
            print(f"Ready for world tour! Planned stops: {world_tour_stops}")
            break
        current_command = command.split(":")


        if current_command[0] == "Add Stop":
            current_index = int(current_command[1])
            current_string = current_command[2]
            world_tour_stops = add_stop(world_tour_stops, current_index, current_string)
        elif current_command[0] == "Remove Stop":
            start_index = int(current_command[1])
            end_index = int(current_command[2])
            world_tour_stops = remove_stop(world_tour_stops, start_index, end_index)
        elif current_command[0] == "Switch":
            old_string = current_command[1]
            new_string = current_command[2]
            world_tour_stops = switch(world_tour_stops, old_string, new_string)



tour_stops = input()
world_tour(tour_stops)
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
