number_of_presents = int(input())
size_of_the_neighborhood = int(input())

matrix = [[row for row in input().split()] for _ in range(size_of_the_neighborhood)]

SANTA = 'S'
NICE_KID = 'V'
COOKIES = 'C'
nice_kids_counter = [sum([matrix[row].count('V') for row in range(size_of_the_neighborhood)])]
nice_kids_got_present = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}


def find_santa():
    for row in range(size_of_the_neighborhood):
        if 'S' in matrix[row]:
            col = matrix[row].index('S')
            matrix[row][col] = '-'                   # позицията на Дядо Коледа се занулява за да се осигурим да не попадаме на него по време на движение

            return row, col


santa_row_position, santa_col_position = find_santa()


def cookie(presents_left, nice_kids):   # Функция за когато Дядо Коледа срещне бисквитка
    for x, y in directions.values():
        r = santa_row_position + x        # установяване на посоките на движение спрямо бисквитката
        c = santa_col_position + y

        if matrix[r][c].isalpha():        # проверява се позицията дали е буква
            if matrix[r][c] == NICE_KID:  # NICE_KID = 'V'
                nice_kids += 1

            matrix[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids



while True:
    command = input()

    if command == 'Christmas morning' or number_of_presents < 1:
        break

    santa_row_position = santa_row_position + directions[command][0]
    santa_col_position = santa_col_position + directions[command][1]

    house_to_be_visited = matrix[santa_row_position][santa_col_position]

    if house_to_be_visited == NICE_KID:       # NICE_KID = 'V'
        nice_kids_got_present += 1
        number_of_presents -= 1

    elif house_to_be_visited == COOKIES:      # COOKIES = 'C'
        number_of_presents, nice_kids_got_present = cookie(number_of_presents, nice_kids_got_present)

    matrix[santa_row_position][santa_col_position] = '-'

    if not number_of_presents or nice_kids_counter[0] == nice_kids_got_present:
        break

matrix[santa_row_position][santa_col_position] = 'S'

if not number_of_presents and nice_kids_got_present < nice_kids_counter[0]:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if nice_kids_counter[0] == nice_kids_got_present:
    print(f"Good job, Santa! {nice_kids_counter[0]} happy nice kid/s.")

else:
    print(f"No presents for {nice_kids_counter[0] - nice_kids_got_present} nice kid/s.")
