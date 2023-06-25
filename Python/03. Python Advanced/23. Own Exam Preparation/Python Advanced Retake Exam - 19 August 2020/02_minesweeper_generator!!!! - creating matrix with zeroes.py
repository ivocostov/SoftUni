def create_minefield(size, mines_count):
    mines_field = [[mine for mine in '0' * size] for _ in range(size)]

    for coordinates in range(mines_count):
        mine = input().replace('(', '').replace(')', '') .split(', ')

        current_mine_row = int(mine[0])
        current_mine_col = int(mine[1])

        mines_field[current_mine_row][current_mine_col] = '*'

    return mines_field


def valid_coordinates(row, col):
    if 0 <= row < mines_field_size and 0 <= col < mines_field_size:
        return True
    return False


def main_logic(matrix, row, col):
    coordinate_sum = 0

    for direction in directions.values():
        check_row_at_direction = int(row) + direction[0]
        check_col_at_direction = int(col) + direction[1]

        if valid_coordinates(check_row_at_direction, check_col_at_direction) and matrix[check_row_at_direction][check_col_at_direction] == '*':
            coordinate_sum += 1
            matrix[row][col] = coordinate_sum


def print_function(matrix):
    [print(*matrix[row]) for row in range(mines_field_size)]


mines_field_size = int(input())
number_of_mines = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "top_left_diagonal": (-1, -1),
    "bottom_left_diagonal": (-1, 1),
    "top_right_diagonal": (1, -1),
    "bottom_right_diagonal": (1, 1),
}


mines_field = create_minefield(mines_field_size, number_of_mines)


for row in range(mines_field_size):
    for col in range(mines_field_size):
        if mines_field[row][col] != '*':
            main_logic(mines_field, row, col)



print_function(mines_field)


