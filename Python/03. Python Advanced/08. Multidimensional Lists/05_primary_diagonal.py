size_of_square_matrix = int(input())

primary_diagonal = []
matrix = []

for num in range(size_of_square_matrix):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for row in range(len(matrix)):
    for col in range(size_of_square_matrix):
        if [row] == [col]:
            value = matrix[row][col]
            primary_diagonal.append(value)

print(sum(primary_diagonal))