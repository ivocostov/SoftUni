def valid_indices(indices):
    if set(indices[:2]).issubset(valid_rows) and set(indices[2:]).issubset(valid_cols):  # проверява дали първите две цифри от подадените
        return True                                                                      # се намират във валидните редици и колони
    return False


def matrix_shuffle(cmd, indices):
    if valid_indices(indices) and cmd == 'swap' and len(indices) == 4:
        row_1, col_1, row_2, col_2 = indices

        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        print(*[' '.join(matrix[row]) for row in range(rows)], sep='\n')

    else:
        print('Invalid input!')


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command, *data = [int(x) if x.isdigit() else x for x in input().split()]

    if command == 'END':
        break

    matrix_shuffle(command, data)
