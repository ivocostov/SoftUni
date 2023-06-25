from functools import reduce
from math import floor

string_expression = input().split()
idx = 0  # променливата пази текущия индекс на който се намираме

operators_dict = {
    '*': lambda i: reduce(lambda a, b: a * b, map(int, string_expression[:i])),  # reduce взима първите два елемента от
    '+': lambda i: reduce(lambda a, b: a + b, map(int, string_expression[:i])),  # листа, извършва действието, което се
    '-': lambda i: reduce(lambda a, b: a - b, map(int, string_expression[:i])),  # изисква от lambda и връща резултата
    '/': lambda i: reduce(lambda a, b: a / b, map(int, string_expression[:i])),  # на мястото на тези две цифри, като
}                                                                                # продължава итерацията със следващото
                                                                                 # число.
while idx < len(string_expression):  # това условие е заради това че дължината на string_expression ще се променя динамично
    symbol = string_expression[idx]

    if symbol in '*+-/':
        result = operators_dict[symbol](idx)  # на речника се подава символа като ключ, и текущия индекс или "i" като параметър
        string_expression[0] = result
        [string_expression.pop(1) for _ in range(idx)]
        idx = 0

    idx += 1
print(int(string_expression[0]))

