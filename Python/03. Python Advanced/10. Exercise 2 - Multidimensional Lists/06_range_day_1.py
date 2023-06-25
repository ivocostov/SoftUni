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

rows, cols = [5, 5]

matrix = [[el for el in input().split()] for _ in range(rows)]

shooter_position = []
total_targets = 0
targets_left = 0
targets_hit = []

for row in range(rows):
    if 'A' in matrix[row]:
        shooter_position = [row, matrix[row].index('A')]
    elif 'x' in matrix[row]:
        targets_left += 1
        total_targets += 1

number_of_commands = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for current_command in range(number_of_commands):
    command = input().split()
    command_in_place = command[0]

    if command_in_place == 'move':
        direction = command[1]
        steps = int(command[2])

        for current_direction, current_coordinates in directions.items():
            if current_direction == direction:
                if current_direction == 'up':
                    target_row, target_col = [shooter_position[1], shooter_position[0] - steps]

                    if 0 <= target_row < rows:
                        if matrix[target_row][target_col] == '.':
                            matrix[shooter_position[0]][shooter_position[1]] = '.'
                            matrix[target_row][target_col] = 'A'

                elif current_direction == 'down':
                    target_row, target_col = [shooter_position[1], shooter_position[0] + steps]

                    if 0 <= target_row < rows:
                        if matrix[target_row][target_col] == '.':
                            matrix[shooter_position[0]][shooter_position[1]] = '.'
                            matrix[target_row][target_col] = 'A'

                elif current_direction == 'left':
                    target_row, target_col = [shooter_position[0], shooter_position[1] - steps]

                    if 0 <= target_col < cols:
                        if matrix[target_col][target_row] == '.':
                            matrix[shooter_position[0]][shooter_position[1]] = '.'
                            matrix[target_row][target_col] = 'A'
                elif current_direction == 'right':
                    target_row, target_col = [shooter_position[0], shooter_position[1] + steps]

                    if 0 <= target_col < cols:
                        if matrix[target_col][target_row] == '.':
                            matrix[shooter_position[0]][shooter_position[1]] = '.'
                            matrix[target_row][target_col] = 'A'

    if command_in_place == 'shoot':
        direction = command[1]

        for current_direction, current_coordinates in directions.items():
            if current_direction == direction:
                if current_direction == 'up' or current_direction == 'down':
                    row_to_shoot_at = shooter_position[0] + current_coordinates[0]
                    if 0 <= row_to_shoot_at < rows:
                        for shot in range(shooter_position[0] + 1, rows):
                            if matrix[shot][shooter_position[1]] == 'x':
                                matrix[shot][shooter_position[1]] = '.'
                                targets_left -= 1
                                targets_hit.append([shot, shooter_position[1]])
                                break

                elif current_direction == 'left':
                    for shot in range(shooter_position[1] - 1, cols - 1, -1):
                        column_to_shoot_at = shot + current_coordinates[1]
                        if 0 <= column_to_shoot_at < rows:
                            if matrix[column_to_shoot_at][shooter_position[0]] == 'x':
                                matrix[column_to_shoot_at][shooter_position[0]] = '.'
                                targets_left -= 1
                                targets_hit.append([column_to_shoot_at, shooter_position[0]])
                                break
                elif current_direction == 'right':
                    column_to_shoot_at = shooter_position[1] + current_coordinates[1]
                    if 0 <= column_to_shoot_at < rows:
                        for shot in range(shooter_position[1] - 1, cols):
                            if matrix[shot][shooter_position[0]] == 'x':
                                matrix[shot][shooter_position[0]] = '.'
                                targets_left -= 1
                                targets_hit.append([shot, shooter_position[0]])
                                break


if targets_left > 0:
    print(f'Training not completed! {targets_left} targets left.')
    print(*targets_hit)
else:
    print(f"Training completed! All {total_targets} targets hit.")
    print(*targets_hit, sep='\n')
