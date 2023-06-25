"""
Input:
3
11 2 4
4 5 6
10 8 -12
----------------------------------------------
4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14

"""


size_of_a_square_matrix = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size_of_a_square_matrix)]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

# primary_diagonal_sum = sum([matrix[row][row] for row in range(size_of_a_square_matrix)])
# secondary_diagonal_sum = sum([matrix[row][size_of_a_square_matrix - row - 1] for row in range(size_of_a_square_matrix)])

for row in range(size_of_a_square_matrix):
    for col in range(size_of_a_square_matrix):
        if row == col:
            primary_diagonal_sum += matrix[row][col]

for backward_row in range(len(matrix) - 1, - 1, -1):
    secondary_diagonal_sum += matrix[backward_row][(len(matrix) - 1) - backward_row]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))
