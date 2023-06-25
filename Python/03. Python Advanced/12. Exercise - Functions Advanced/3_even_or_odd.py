# def even_odd(*args):
#     condition = args[-1]
#     if condition == 'even':
#         return [num for num in args[:-1] if n % 2 == 0]
#
#     elif condition == 'odd':
#         return [num for num in args[:-1] if n % 2 != 0]



def even_odd(*args):
    numbers = []
    condition = args[-1]

    for num in args[:-1]:
        if condition == 'even':
            if num % 2 == 0:
                numbers.append(num)
        elif condition == 'odd':
            if num % 2 == 1:
                numbers.append(num)
    return numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))