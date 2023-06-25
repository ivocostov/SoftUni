"""
Inputs:           Outputs:
5                    1
0K0K0
K000K
00K00
K000K
0K0K0
------------------
2                    0
KK
KK
------------------
8                   12
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
=======================
Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task - the Knight.
A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column, or diagonal.
(e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically -
i.e., in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights that can attack one another
with one move are left.
Always remove the knight who can attack the greatest number of knights. If there are two or more knights with the same number of attacks, remove the top-left one.
Input
•	On the first line, you will receive integer N - the size of the board
•	On the following N lines, you will receive strings with "K" and "0"
Output
•	Print a single integer with the number of knights that need to be removed.
Constraints
•	The size of the board will be 0 < N < 30
•	Time limit: 0.3 sec. Memory limit: 16 MB
"""


size_of_matrix = int(input())

matrix = [list(input()) for _ in range(size_of_matrix)]  # каства се към лист защото входа е стринг и няма по какво да се сплитне
                                                         #
directions = (
    (-2, -1),  # move up(2) and left(1)   ROWS ANS COLS
    (-2, 1),  # move up(2) and right(1)   ROWS ANS COLS
    (-1, -2),  # move up(1) and left(2)   ROWS ANS COLS
    (-1, 2),  # move up(1) and right(2)   ROWS ANS COLS
    (2, -1),  # move down(2) and left(1)   ROWS ANS COLS
    (2, 1),  # move down(2) and right(1)   ROWS ANS COLS
    (1, -2),  # move down(1) and left(2)   ROWS ANS COLS
    (1, 2)  # move down(1) and right(2)   ROWS ANS COLS
)

removed_knights = 0

while True:
    max_attacks = 0                      # максимум брой атаки на коня намерен досега
    knight_that_has_most_attacks = []    # позицията на коня с най-много атаки намерен до сега

    for row in range(size_of_matrix):
        for col in range(size_of_matrix):
            if matrix[row][col] == 'K':  # ако сме попаднали на кон
                attacks = 0              # брой атаки за текущия кон

                for direction in directions:
                    direction_row = row + direction[0]  # взима се позицията на индекс 0 от тюпъла в directions, отговаря за редовете
                    direction_col = col + direction[1]  # взима се позицията на индекс 1 от тюпъла в directions, отговаря за колоните

                    if 0 <= direction_row < size_of_matrix and 0 <= direction_col < size_of_matrix:  # валидира се позицията на коня да не излиза извън размера на дъската при движение
                        if matrix[direction_row][direction_col] == 'K':          # ако на позицията на която се движим има кон
                            attacks += 1                                         # увеличи атаката с едно на текущия кон
                if attacks > max_attacks:                      # ако атаките на текущия кон са по-големи от намерените атаки до момента
                    knight_that_has_most_attacks = [row, col]  # коня, който има най-много атаки се намира на позиция row, col
                    max_attacks = attacks                      # и съответно максималните атаки са равни на текущите атаки


    if knight_that_has_most_attacks:  # ако има нещо в този списък, защото очевидно ако списъка си е останал празен не сме намерили кон, който може да атакува други коне
        matrix[knight_that_has_most_attacks[0]][knight_that_has_most_attacks[1]] = '0'  # коня на тази позиция се маха от дъската
        removed_knights += 1
    else:
        break  # ако списъка с позицията на коня е останал празен то брейкваме

print(removed_knights)
