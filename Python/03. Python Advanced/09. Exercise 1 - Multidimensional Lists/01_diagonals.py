"""
Input:
3
1, 2, 3
4, 5, 6
7, 8, 9

"""


rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

primary_diagonal = []
secondary_diagonal = []

# primary = [matrix[row][row] for row in range(rows)]             # с компрехеншън без primary_diagonal = [] и secondary_diagonal = []
# secondary = [matrix[row][rows - row - 1] for row in range(rows - 1, -1, -1)]    # с компрехеншън без primary_diagonal = [] и secondary_diagonal = []

for row in range(len(matrix)):
    for col in range(rows):
        if [row] == [col]:
            primary_diag_value = matrix[row][col]
            primary_diagonal.append(primary_diag_value)

for backward_row in range(len(matrix) - 1, -1, -1):
    secondary_diag_value = matrix[backward_row][(len(matrix) - 1) - backward_row]
    secondary_diagonal.append(secondary_diag_value)

# print(f"Primary diagonal: {', '.join(str(x) for x in primary)} Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)} Sum: {sum(secondary)}")

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal[::-1]))}. Sum: {sum(secondary_diagonal)}")
