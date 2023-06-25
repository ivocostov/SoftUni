SIZE_OF_CHESSBOARD = 8

queens_position = []

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


def create_chessboard(size):
    return [[row for row in input().split()] for _ in range(size)]


def valid_coordinates(row, col):
    if 0 <= row < SIZE_OF_CHESSBOARD and 0 <= col < SIZE_OF_CHESSBOARD:
        return True
    return False


def find_king(matrix):
    for row in range(SIZE_OF_CHESSBOARD):
        if 'K' in matrix[row]:
            col = matrix[row].index('K')

            return row, col


def check_if_king_can_be_taken(matrix, king_row, king_col):
    for direction, coordinates in directions.items():
        check_row = king_row + coordinates[0]  # row + col
        check_col = king_col + coordinates[1]  # col + row
        for check_in_direction in range(SIZE_OF_CHESSBOARD):
            if valid_coordinates(check_row, check_col):
                if matrix[check_row][check_col] == 'Q':
                    queens_position.append([check_row, check_col])
                    break

                check_row += directions[direction][0]
                check_col += directions[direction][1]

            else:
                break



chessboard = create_chessboard(SIZE_OF_CHESSBOARD)
king_position = list(find_king(chessboard))
check_if_king_can_be_taken(chessboard, king_position[0], king_position[1])

if queens_position:
    for queen in queens_position:
        print(queen)

else:
    print("The king is safe!")
