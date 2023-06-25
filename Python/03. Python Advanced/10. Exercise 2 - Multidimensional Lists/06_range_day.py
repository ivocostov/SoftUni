"""
You are participating in a Firearm course. It is a training day at the shooting range.
You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
•	Your position is marked with the symbol "A"
•	Targets marked with symbol "x"
•	All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
•	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move
if the field you want to step on is marked with ".".
•	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only
the nearest target. When you have shot a target, the field becomes empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
•	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
•	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Input
•	5 lines representing the field (symbols, separated by a single space)
•	N - count of commands
•	On the following N lines - the commands in the format described above
Output
•	On the first line, print one of the following:
o	If all the targets were shot
"Training completed! All {count_targets} targets hit."
o	Otherwise:
              	       "Training not completed! {count_left_targets} targets left."
•	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
Constrains
•	All the commands will be valid
•	There will always be at least one target


Inputs:

. . . . .
x . . . .
. A . . .
. . . x .
. x . . x
3
shoot down
move right 4
move left 1
---------------------
. . . . .
. . . . .
. A x . .
. . . . .
. x . . .
2
shoot down
=======================
Outputs:

Training not completed! 3 targets left.
[4, 1]
--------------------------------------------
Training completed! All 2 targets hit.
[4, 1]
[2, 2]

"""
MATRIX_SIZE = 5

matrix = [[el for el in input().split()] for _ in range(MATRIX_SIZE)]

total_targets = [sum([matrix[row].count('x') for row in range(MATRIX_SIZE)])]
targets_hit = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}


def valid_coordinates(row, col):
    if 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE:
        return True

'''Ако се подадат две валидни посоки една след друга не се сменя позицията'''
def moving_command(shooter_row_position, shooter_col_position, direction, steps_to_move):
    moving_row_position = shooter_row_position + directions[direction][0] * int(steps_to_move)
    moving_col_position = shooter_col_position + directions[direction][1] * int(steps_to_move)

    if valid_coordinates(moving_row_position, moving_col_position) and matrix[moving_row_position][moving_col_position] == '.':
        matrix[shooter_row_position][shooter_col_position] = '.'
        matrix[moving_row_position][moving_col_position] = 'A'

        return moving_row_position, moving_col_position
    return shooter_row_position, shooter_col_position


def shooting_command(shooter_row_position, shooter_col_position, direction):
    for shoot in range(MATRIX_SIZE):
        row_to_shoot_at = shooter_row_position + directions[direction][0]
        col_to_shoot_at = shooter_col_position + directions[direction][1]
        if valid_coordinates(row_to_shoot_at, col_to_shoot_at):
            if matrix[row_to_shoot_at][col_to_shoot_at] == 'x':
                targets_hit.append([row_to_shoot_at, col_to_shoot_at])
                total_targets[0] -= 1
                matrix[row_to_shoot_at][col_to_shoot_at] = '.'
                break
            shooter_row_position = row_to_shoot_at  # giving new values to the function and iterate again
            shooter_col_position = col_to_shoot_at  #

        else:          # if there is not valid coordinates
            break


def show_results():
    if total_targets[0] > 0:
        print(f'Training not completed! {total_targets[0]} targets left.')
        [print(x) for x in targets_hit]
    else:
        print(f"Training completed! All {len(targets_hit)} targets hit.")
        [print(x) for x in targets_hit]



def find_shooter_position():
    for shooter_row_pos in range(MATRIX_SIZE):
        if 'A' in matrix[shooter_row_pos]:
            shooter_col_pos = matrix[shooter_row_pos].index('A')

            return shooter_row_pos, shooter_col_pos


shooter_row_position, shooter_col_position = find_shooter_position()




number_of_commands = int(input())

for current_cmd_number in range(number_of_commands):
    command = input().split()

    if command[0] == 'move':
        direction = command[1]
        steps_to_move = command[2]
        moving_command(shooter_row_position, shooter_col_position, direction, steps_to_move)


    elif command[0] == 'shoot':
        direction = command[1]
        shooting_command(shooter_row_position, shooter_col_position, direction)


show_results()