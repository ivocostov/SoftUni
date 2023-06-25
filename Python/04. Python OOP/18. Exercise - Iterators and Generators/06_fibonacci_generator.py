""" Винаги първите две числа в поредицата на Фибоначи трябва да са 0 и 1. ТРЕТОТО число се явява сбор на първото (0) и второто число (1).
ЧЕТВЪРТОТО число е сбор от второто (1) и ТРЕТОТО число(1), ПЕТОТО е сбор на третото(1) и ЧЕТВЪРТОТО число (2) и т.н """

def fibonacci():
    first_number, second_number = 0, 1

    while True:
        yield first_number  # отпечатва се първото задължително число от Fibonacci sequence

        first_number, second_number = second_number, first_number + second_number  # първото число става равно на второто
                                                                                   # а второто става равно на сбора на първото и второто число


generator = fibonacci()
for i in range(7):
    print(next(generator))

# 0
# 1
# 1
# 2
# 3
# 5
# 8