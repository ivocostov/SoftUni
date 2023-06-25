rows, cols = [int(x) for x in input().split(', ')]

current_nums_input = []
matrix_sum = 0

for numbers in range(rows):
    numbers_in = [int(x) for x in input().split(', ')]
    current_nums_input.append(numbers_in)

for current_list in current_nums_input:
    current_sum = sum(current_list)
    matrix_sum += current_sum
print(matrix_sum)
print(current_nums_input)