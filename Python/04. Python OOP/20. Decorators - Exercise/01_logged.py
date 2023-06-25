def logged(func):               # приема се референция към функцията

    def wrapper(*args):

        """ Връщаме името на функцията в първата променлива, след това във втората итерираме през *args и връщаме всеки един аргумент като str и накрая
        в последната променлива извикваме изпълнената функция func """

        return f"you called {func.__name__}" \
               f"({', '.join(str(arg) for arg in args)})\n" \
               f"it returned {func(*args)}"

    return wrapper



@logged
def func(*args):
    return 3 + len(args)

print(func(4, 4, 4))


# @logged
# def sum_func(a, b):
#     return a + b
#
# print(sum_func(1, 4))
