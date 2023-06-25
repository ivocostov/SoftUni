"""
Inputs:

3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
---------------------------
4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
===========================
Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N.
You will get elements for each column on the following N lines, separated with a single space. You will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.

"""


def check_for_valid_input(current_row, current_col):
    if 0 <= current_row < rows and 0 <= current_col < rows:
        return True
    return False


def matrix_modification(cmd, info):
    current_row = int(info[0])
    current_col = int(info[1])
    value = info[-1]
    if check_for_valid_input(current_row, current_col):
        if cmd == 'Add':
            matrix[current_row][current_col] += value

        elif cmd == 'Subtract':
            matrix[current_row][current_col] -= value

    else:
        print('Invalid coordinates')


rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command, *data = [int(x) if x.isdigit() else x for x in input().split()]

    if command == 'END':
        [print(*row) for row in matrix]
        break

    matrix_modification(command, data)
