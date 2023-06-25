rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float("-inf")  # щом се търси максимална стойност то трябва да се зададе възможно най малкото, в случая -infinity
biggest_matrix = []

for row in range(rows - 2):       # rows - 2 защото не се стига до последните два реда, тъй като няма смисъл, търси се матрица 3х3
    for col in range(cols - 2):   # cols - 2 защото не се стига до последните две колони, тъй като няма смисъл, търси се матрица 3х3
        first_row = [row][col:col + 3]  # взимане на числата от реда от колоната до колоната + 3
        second_row = [row + 1][col:col + 3]
        third_row = [row + 2][col:col + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*biggest_matrix[row]) for row in range(3)]