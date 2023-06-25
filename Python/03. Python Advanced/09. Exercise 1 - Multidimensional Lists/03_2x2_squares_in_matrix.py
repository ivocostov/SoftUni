rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

equal_symbols = 0

for row in range(rows - 1):  # rows - 1 е защото не се стига до последния ред тъй като не може да се продължи надолу (търси се матрица 2х2) и да не гръмне по индекс тъй като няма следващ ред
    for col in range(cols - 1):  # същата причина като по-горе
        symbol = matrix[row][col]
        if matrix[row][col + 1] == symbol and matrix[row + 1][col] == symbol and matrix[row + 1][col + 1] == symbol:  # проверка дали символа вдясно, отдолу и по диагонал е същия
            equal_symbols += 1


print(equal_symbols)