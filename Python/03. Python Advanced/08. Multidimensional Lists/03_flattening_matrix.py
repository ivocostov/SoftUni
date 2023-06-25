rows = int(input())

flattened_matrix = []

for numbers in range(rows):
    data = [int(x) for x in input().split(', ')]
    for num in data:
        flattened_matrix.append(num)

print(flattened_matrix)