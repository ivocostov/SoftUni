"""
Your task is to collect as many eggs as possible.
On the first line, you will be given a number representing the size of the field. On the following few lines, you will be given a field with:
•	One bunny - randomly placed in it and marked with the symbol "B"
•	Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
The directions that should be considered as possible are up, down, left, and right.
If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction.
For more clarifications, see the examples below.
Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
Input
•	A number representing the size of the field
•	The matrix representing the field (each position separated by a single space)
Output
•	The direction which should be considered as best (lowercase)
•	The field positions from which we are collecting eggs as lists
•	The total number of eggs collected
Constraints
•	There will NOT be two or more paths consisting of the same total amount of eggs.

Inputs:

5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
------------------
8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
==============================
Outputs:
right
[3, 1]
[3, 2]
[3, 3]
[3, 4]
87
-------------------
down
[6, 2]
[7, 2]
113

"""


size_of_the_matrix = int(input())
matrix = [list(input().split()) for _ in range(size_of_the_matrix)]


bunny_position = []  # позицията(координатите) на заека
max_collectable_eggs = 0  # брой на яйцата които могат да се съберат
path_with_most_eggs = []  # координатите на пътя с най-много яйца
direction_with_most_eggs = None  # тук ще се пази стринг

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

'''
Намираме къде е заека!
'''
for row in range(size_of_the_matrix):
    if 'B' in matrix[row]:
        bunny_position = [row, matrix[row].index("B")]  # row and col

'''
Движение на заека!
'''
for current_direction, coordinates in directions.items():
    row, col = [
        bunny_position[0] + coordinates[0],  # от позицията на заека + реда (нагоре или надолу)
        bunny_position[1] + coordinates[1]   # от позицията на заека + колоната (наляво или надясно)
    ]
    eggs_path = []  # тук се пазят координатите на текущия път
    collected_eggs = 0  # пазят се текущо събраните яйца

    while 0 <= row < size_of_the_matrix and 0 <= col < size_of_the_matrix:
        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        eggs_path.append([row, col])

        row += coordinates[0]  # увеличаване на позицията в посоката в която се движим
        col += coordinates[1]  # увеличаване на позицията в посоката в която се движим

    if collected_eggs >= max_collectable_eggs:
        max_collectable_eggs = collected_eggs
        direction_with_most_eggs = current_direction
        path_with_most_eggs = eggs_path

print(direction_with_most_eggs)
print(*path_with_most_eggs, sep='\n')
print(max_collectable_eggs)
