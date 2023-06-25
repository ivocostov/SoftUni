def create_matrix(size):
    matrix = [[row for row in input()] for _ in range(matrix_size)]
    return matrix


def main_logic(matrix):
    snake_position = []
    food_quantity = 0
    out_of_territory = False

    for current_row in range(matrix_size):
        if 'S' in matrix[current_row]:
            snake_position.append(int(current_row))
            snake_position.append(int(matrix[current_row].index('S')))
            matrix[snake_position[0]][snake_position[1]] = '.'

    while True:
        command = input()

        targeted_row = snake_position[0] + directions[command][0]
        targeted_col = snake_position[1] + directions[command][1]


        if not 0 <= targeted_row < matrix_size or not 0 <= targeted_col < matrix_size:
            out_of_territory = True
            break

        else:
            targeted_position = matrix[targeted_row][targeted_col]

        if targeted_position == '*':
            food_quantity += 1
            matrix[targeted_row][targeted_col] = '.'
            if food_quantity == 10:
                snake_position[0], snake_position[1] = targeted_row, targeted_col
                break

        elif targeted_position == 'B':
            burrow_up_coordinates, burrow_down_coordinates = [(row, matrix[row].index('B')) for row in range(len(matrix)) if 'B' in matrix[row]]

            matrix[targeted_row][targeted_col] = '.'

            if tuple(snake_position) == burrow_up_coordinates:
                matrix[burrow_down_coordinates[0]][burrow_down_coordinates[1]] = '.'
                snake_position = [burrow_down_coordinates[0], burrow_down_coordinates[1]]

            else:
                matrix[burrow_down_coordinates[0]][burrow_down_coordinates[1]] = '.'
                snake_position = [burrow_down_coordinates[0], burrow_down_coordinates[1]]
                continue

        matrix[targeted_row][targeted_col] = '.'
        snake_position[0], snake_position[1] = targeted_row, targeted_col

    return matrix, food_quantity, out_of_territory, snake_position


def print_function(data):
    matrix, food_quantity, out_of_territory, snake_position = data

    if out_of_territory:
        print("Game over!")
        print(f"Food eaten: {food_quantity}")

    elif food_quantity == 10:
        print("You won! You fed the snake.")
        print(f"Food eaten: {food_quantity}")
        matrix[snake_position[0]][snake_position[1]] = 'S'

    [print(''.join(row)) for row in matrix]


matrix_size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = create_matrix(matrix_size)

print_function(main_logic(matrix))  # ИЗВИКВА ОСНОВНАТА ФУНКЦИЯ И СЛЕД КАТО ТЯ СЕ ИЗПЪЛНИ ИЗВИКВА ФУНКЦИЯТА ЗА ПЕЧАТ
