rows = int(input())

matrix = []

for numbers in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append([])
    for num in data:
        if num % 2 == 0:
            matrix[-1].append(num)

print(matrix)