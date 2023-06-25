# size = int(input())
#
# for x in range(size):
#     space_data = size - x - 1  # тук се обработват празните полета около звездичките
#     stars_data = x + 1
#     print(' ' * space_data + '* ' * stars_data)
#
# for x in range(size - 2, -1, -1):
#     space_data = size - x - 1
#     stars_data = x + 1
#     print(' ' * space_data + '* ' * stars_data)

'''

Функциите по-долу се преизползват каквато е идеята на ООП

'''


def choose_pattern():
    pattern = input('Choose type of pattern -> \nTriangle\nRhombus\nSquare\nPattern choice:')
    size_of_pattern = int(input('Enter pattern size: '))
    return pattern, size_of_pattern


def print_patterns(space_data, stars_data):
    print(' ' * space_data + '* ' * stars_data)



# size = int(input())


def get_pattern_data(*data):
    pattern, size = data

    if pattern == 'Rhombus':
        for x in range(size):
            space_data = size - x - 1  # тук се обработват празните полета около звездичките
            stars_data = x + 1
            print_patterns(space_data, stars_data)

        for x in range(size - 2, -1, -1):
            space_data = size - x - 1  # тук се обработват празните полета около звездичките
            stars_data = x + 1
            print_patterns(space_data, stars_data)

    elif pattern == 'Triangle':
        for x in range(size):
            stars_data = x + 1
            print_patterns(0, stars_data)


    elif pattern == 'Square':
        for x in range(size):
            print_patterns(0, size)




get_pattern_data(*choose_pattern())  # ако звездичката я няма ще върне tuple