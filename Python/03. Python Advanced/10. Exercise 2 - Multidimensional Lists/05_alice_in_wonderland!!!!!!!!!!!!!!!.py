"""
Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines,
you will receive the rows of the territory:
•	Alice will be placed in a random position, marked with the letter "A".
•	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position,
she collects the tea bags and increases the quantity with the corresponding number.
•	There will always be one rabbit hole on the territory marked with the letter "R".
•	All of the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting.
Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.
Input
•	On the first line, you will be given the integer n – the size of the square matrix
•	On the following n lines - matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will be given a move command
Output
•	On the first line:
o	If Alice steps on the rabbit hole or she go out of the territory, print:
"Alice didn't make it to the tea party."
o	If she collected at least 10 bags of tea, print:
"She did it! She went to the party."
•	On the following lines, print the matrix.
Constraints
•	Alice will always either go outside the Wonderland or collect 10 bags of tea
•	All the commands will be valid
•	All of the given numbers will be valid integers in the range [0, 10]


Inputs:

5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
------------------------
7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right
========================
Outputs:

Alice didn't make it to the tea party.
. * . . 1
* * * . .
4 * . 1 .
. . . 2 .
. 3 . . .

-----------------------
She did it! She went to the party.
* * . 1 1 . .
* . . . 6 . 5
* * . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2

"""

size_of_the_matrix = int(input())

matrix = [list(input().split()) for _ in range(size_of_the_matrix)]

alice_position = []
max_collectable_teabags = 10
collected_teabags_so_far = 0
teabags_collected = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for current_row in range(size_of_the_matrix):
    if 'A' in matrix[current_row]:
        alice_position = [current_row, matrix[current_row].index('A')]
        matrix[current_row][alice_position[1]] = '*'


while collected_teabags_so_far < max_collectable_teabags:
    direction_command = input()

    direction_row = alice_position[0] + directions[direction_command][0]
    direction_col = alice_position[1] + directions[direction_command][1]

    if not (0 <= direction_row < size_of_the_matrix and 0 <= direction_col < size_of_the_matrix):
        break

    if matrix[direction_row][direction_col] == 'R':
        matrix[direction_row][direction_col] = '*'
        break

    elif matrix[direction_row][direction_col] == '.':
        matrix[direction_row][direction_col] = '*'
        alice_position = [direction_row, direction_col]

    elif matrix[direction_row][direction_col] == '*':
        alice_position = [direction_row, direction_col]

    else:
        collected_teabags_so_far += int(matrix[direction_row][direction_col])
        matrix[direction_row][direction_col] = '*'
        alice_position = [direction_row, direction_col]

if collected_teabags_so_far < max_collectable_teabags:
    print("Alice didn't make it to the tea party.")
    [print(*row) for row in matrix]

else:
    print('She did it! She went to the party.')
    [print(*row) for row in matrix]
