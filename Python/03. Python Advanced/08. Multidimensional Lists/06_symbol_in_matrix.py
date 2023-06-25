matrix_size = int(input())

matrix = []
found_symbol = False

for nums in range(matrix_size):
    numbers = [letter for letter in input()]
    matrix.append(numbers)

searched_symbol = input()

for row in range(len(matrix)):
    for col in range(len(matrix)):
        symbol = matrix[row][col]
        if symbol == searched_symbol:
            found_symbol = True
            print(f'({row}, {col})')
            break
    if found_symbol:
        break
if not found_symbol:
    print(f"{searched_symbol} does not occur in the matrix")