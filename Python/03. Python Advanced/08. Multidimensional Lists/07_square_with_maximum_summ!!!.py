"""
Примерен Вход:
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0

"""

rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

SQUARE_SIZE = 2
sum_of_max_numbers = {
    "max_number": -1000000,
    "row": 0,
    "col": 0
}


# Проверка на валидност на индекс или дали сме в диапазона на матрицата!
def check_valid_index(row, col):
    if 0 <= row + SQUARE_SIZE <= rows and 0 <= col + SQUARE_SIZE <= cols:  # диапазона е row + 2 и col + 2, защото се иска да взимаме само по 2 числа
        return True

# Сумиране на числата в зададения диапазон от текущ ред и колона
def sum_square(row, col):
    if check_valid_index(row, col):
        numbers_sum = 0
        for row_check in range(row, row + SQUARE_SIZE):
            numbers_sum += sum(matrix[row_check][col: col + SQUARE_SIZE])
        if sum_of_max_numbers["max_number"] < numbers_sum:   # Ако максималната сума е по-голяма от зададената в речника
            sum_of_max_numbers["max_number"] = numbers_sum   # то зададената сума в речника става равна на максималната.
            sum_of_max_numbers["row"] = row                  # Подава се текущия ред на речника
            sum_of_max_numbers["col"] = col                  # Подава се текущата колона на речника


# Този цикъл подава на горната функция редовете и колоните!!!
for row in range(rows):
    for col in range(cols):
        sum_square(row, col)

for row in range(sum_of_max_numbers["row"], sum_of_max_numbers["row"] + SQUARE_SIZE):         # В обхват от реда запазен в речника до реда + 2
    print(*matrix[row][sum_of_max_numbers["col"]:sum_of_max_numbers["col"] + SQUARE_SIZE])    # (т.е. две поредни числа)
print(sum_of_max_numbers["max_number"])                                                       # изпринтирай числата намиращи се
                                                                                              # на този ред в установения обхват
                                                                                              # от колоната запазена в речника
                                                                                              # до колоната + 2 (т.е. две поредни числа)