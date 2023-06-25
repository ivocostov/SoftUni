def type_check(variable_type):
    def decorator(func):                                # тук се получава функцията ** times2 **
        def wrapper(*args):                             # тук се получават аргументите на ** times2 **
            for arg in args:
                if isinstance(arg, variable_type):
                    return func(*args)

            return "Bad Type"
        return wrapper
    return decorator

#
# @type_check(int)
# def times2(num):
#     return num*2
#
#
# print(times2(2))
# print(times2('Not A Number'))

# ----------------------------------

@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


