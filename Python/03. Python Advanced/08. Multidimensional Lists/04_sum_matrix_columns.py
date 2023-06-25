rows, cols = [int(x) for x in input().split(', ')]

matrix = []
column_sum = 0

for number in range(rows):
    matrix.append([int(x) for x in input().split()])

for i in range(cols):
    for j in range(rows):
        column_sum += matrix[j][i]
    print(column_sum)
    column_sum = 0