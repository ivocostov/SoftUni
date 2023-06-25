playground_rows, playground_cols = [int(x) for x in input().split()]


playground = [[row for row in input().split()] for _ in range(playground_rows)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def find_player(matrix):
    for current_row in range(playground_rows):
        if 'B' in matrix[current_row]:
            current_col = matrix[current_row].index('B')
            matrix[current_row][current_col] = '-'

            return current_row, current_col


def valid_coordinates(row, col):
    if 0 <= row < playground_rows and 0 <= col < playground_cols:
        return True
    return False


def main_logic(matrix):
    player_row_pos, player_col_pos = find_player(playground)

    touched_players = 0
    moves_count = 0

    while True:
        command = input()
        if command == 'Finish' or touched_players == 3:
            break

        move_to_row = player_row_pos + directions[command][0]
        move_to_col = player_col_pos + directions[command][1]
        check_what_is_on_coordinates = matrix[move_to_row][move_to_col]

        if valid_coordinates(move_to_row, move_to_col):
            if check_what_is_on_coordinates == 'O':
                continue

            elif check_what_is_on_coordinates == 'P':
                touched_players += 1
                moves_count += 1
                matrix[move_to_row][move_to_col] = '-'
                player_row_pos, player_col_pos = move_to_row, move_to_col

            elif check_what_is_on_coordinates == '-':
                moves_count += 1
                player_row_pos, player_col_pos = move_to_row, move_to_col

    return f"Game over!\nTouched opponents: {touched_players} Moves made: {moves_count}"


print(main_logic(playground))
