cartoon_names = input().split(', ')

players = [{'name': n, 'hit_a_wall': False} for n in cartoon_names]


MAZE_ROWS = 6
#MATRIX_COLS = 6

maze = [[row for row in input().split()] for _ in range(MAZE_ROWS)]


while True:
    current_coordinates = input().split(', ')
    coordinates = []

    current_player = players.pop(0)

    for first_symbol, second_symbol in current_coordinates:
        if first_symbol.isdigit():
            coordinates.append(first_symbol)
        else:
            coordinates.append(second_symbol)

    row, col = int(coordinates[0]), int(coordinates[1])
    target_coordinate = maze[row][col]

    if current_player['hit_a_wall']:
        current_player['hit_a_wall'] = False


    elif target_coordinate == 'E':
        winning_player = current_player['name']
        print(f"{winning_player} found the Exit and wins the game!")

        break

    elif target_coordinate == 'T':
        winning_player = players[0]['name']
        loosing_player = current_player['name']
        print(f"{loosing_player} is out of the game! The winner is {winning_player}.")

        break

    elif target_coordinate == 'W':
        print(f"{current_player['name']} hits a wall and needs to rest.")
        current_player['hit_a_wall'] = True


    players.append(current_player)