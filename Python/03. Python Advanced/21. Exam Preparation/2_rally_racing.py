def create_matrix(size):
    matrix = []

    for _ in range(size):
        row = input().split()
        matrix.append(row)

    return matrix


def main_game_logic(matrix):
    car_coordinates = [0, 0]
    tunnel_up_coordinates, tunnel_down_coordinates = [(i, matrix[i].index('T')) for i in range(len(matrix)) if 'T' in matrix[i]]  # ????
    distance = 0
    finish_condition = False

    while True:
        command = input()

        if command == 'End':
            matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
            return matrix, distance, finish_condition

        elif command == 'up':
            car_coordinates[0] -= 1

        elif command == 'down':
            car_coordinates[0] += 1

        elif command == 'left':
            car_coordinates[1] -= 1

        elif command == 'right':
            car_coordinates[1] += 1

        if matrix[car_coordinates[0]][car_coordinates[1]] == 'T':
            matrix[car_coordinates[0]][car_coordinates[1]] = '.'

            if tuple(car_coordinates) == tunnel_up_coordinates:                             # ако се влиза отгоре на тунела
                matrix[tunnel_down_coordinates[0]][tunnel_down_coordinates[1]] = '.'        # долните координати на тунела става '.'
                car_coordinates = [tunnel_down_coordinates[0], tunnel_down_coordinates[1]]

            else:                                                                            # ако се влиза отдолу на тунела
                matrix[tunnel_down_coordinates[0]][tunnel_down_coordinates[1]] = '.'         # горните координати на тунела става '.'
                car_coordinates = [tunnel_down_coordinates[0], tunnel_down_coordinates[1]]

            distance += 30
            continue

        elif matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
            finish_condition = True
            distance += 10
            matrix[car_coordinates[0]][car_coordinates[1]] = 'C'

            return matrix, distance, finish_condition

        distance += 10


def print_func(data, racing_num):
    matrix, distance, finish_condition = data

    if finish_condition:
        print(f"Racing car {racing_num} finished the stage!")
    else:
        print(f"Racing car {racing_num} DNF.")

    print(f"Distance covered {distance} km.")

    for row in matrix:
        print(''.join(row))


matrix_size = int(input())
racing_car_number = input()

matrix = create_matrix(matrix_size)

print_func(main_game_logic(matrix), racing_car_number)
