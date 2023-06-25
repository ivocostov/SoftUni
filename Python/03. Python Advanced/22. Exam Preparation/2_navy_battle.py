battlefield_size = int(input())

battlefield = [[row for row in input()] for _ in range(battlefield_size)]
sub_position = []

naval_mines = 0
cruisers_hit = 0


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def find_my_sub():
    for row in range(battlefield_size):
        if 'S' in battlefield[row]:
            col = battlefield[row].index('S')
            sub_position.append(row)
            sub_position.append(col)
            battlefield[row][col] = '-'

            return row, col


find_my_sub()


def main_logic(directions, matrix, sub_position):
    global naval_mines
    global cruisers_hit

    while naval_mines < 3 and cruisers_hit < 3:


        command = input()

        targeted_row = sub_position[0] + directions[command][0]
        targeted_col = sub_position[1] + directions[command][1]

        if matrix[targeted_row][targeted_col] == '*':
            naval_mines += 1
            matrix[targeted_row][targeted_col] = '-'

        elif matrix[targeted_row][targeted_col] == 'C':
            cruisers_hit += 1
            matrix[targeted_row][targeted_col] = '-'

        sub_position[0], sub_position[1] = targeted_row, targeted_col

    return matrix, sub_position[0], sub_position[1]


main_logic(directions, battlefield, sub_position)




if naval_mines == 3:
    battlefield[sub_position[0]][sub_position[1]] = 'S'
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{sub_position[0]}, {sub_position[1]}]!")
    [print(*row, sep='') for row in battlefield]

if cruisers_hit == 3:
    battlefield[sub_position[0]][sub_position[1]] = 'S'
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    [print(*row, sep='') for row in battlefield]

