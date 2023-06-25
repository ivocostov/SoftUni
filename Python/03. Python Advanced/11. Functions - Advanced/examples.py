# # # lst = [1, 2, 3, 4, 5]  #
# # # #a, b, *c = lst  # разпакетира първия, втория и всички останали елементи от листа в съответните променливи
# # # a, *_, e = lst  # взима само първия и последния елемент от листа и не разпечатва нищо по средата
# # #
# # #
# # # """
# # # PACKING ARGUMENTS
# # # """
# # #
# # # # Packing for positional arguments - *args, като не е задължително да се казва *args
# # #
# # #
# # # def example_func(*args, **kwargs):  # звездичката пред args взима всички аргументи подадени на функцията, използва се когато не се знае
# # #     print(args)                     # колко аргумента ще бъдат подадени
# # #     print(kwargs)                   # Ако е без звездичка ще приеме само един аргумент.
# # #
# # #
# # # example_func([1, 2, 3, 4], 'text', 123)  # отива в *args
# # #
# # #
# # # # Packing for dictionaries - **kwargs, като не е задължително да се казва *kwargs
# # #
# # # example_func(name='Ivo', age=44, gender='M')  # отива в **kwargs
# # # example_func(language='Python')
# # # example_func(1, 2, 3, 4, ages=[1, 2, 3, 4], names=['Ivan', 'Pesho'])  # 1, 2, 3, 4 отива в *args, останалото в **kwargs
# # #
# # # ########################################################################################################################
# # #
# # # # Example:
# # #
# # # shopping_list = {}
# # #
# # #
# # # def show_list(shopping_list, include_quantities=True):  # include_quantities указва дали да се принтират количествата или не
# # #     print()
# # #     for item_name, quantity in shopping_list.items():
# # #         if include_quantities:
# # #             print(f'{quantity} x {item_name}')
# # #         else:
# # #             print(item_name)
# # #
# # #
# # # def add_items(shopping_list, **things_to_buy):
# # #     for item_name, quantity in things_to_buy.items():
# # #         shopping_list[item_name] = quantity
# # #     return shopping_list
# # #
# # #
# # # shopping_list = add_items(shopping_list, coffee=1, tea=2, cake=1, bread=3)
# # # show_list(shopping_list, include_quantities=True)
# # #
# # # ########################################################################################################################
# # #
# # #
# # # def example_func(a, b, c, *args, **kwargs):
# # #     print(a, b, c)
# # #
# # #
# # # example_func(1, 2, 3, [1, 2, 3], names=['Gosho', 'Pesho'])
# # #
# # # ########################################################################################################################
# # #
# # # a, b, *_ = [1, 2, 3, 4, 5]
# # # print(a, b, _)
# # #
# # # ########################################################################################################################
# # #
# # # my_dict = {'one': 1, 'two': 2, 'three': 3}
# # #
# # # a, b, c = my_dict.items()
# # # # a, b, c = my_dict.keys()
# # # # a, b, c = my_dict.values()
# # #
# # # print(a, b, c)
# # #
# # # ########################################################################################################################
# # #
# # #
# # # def product(n1, n2, n3):
# # #     return n1 * n2 * n3
# # #
# # #
# # # numbers = [10, 5, 3]
# # # print(product(*numbers))  # UNPACKING LISTS
# # #
# # # ########################################################################################################################
# # #
# # # def func(*args, **kwargs):
# # #     print(f'Args: {args}, Kwargs: {kwargs}')
# # #
# # #
# # # func(*[1, 2, 3], **{'site': 'www.softuni.bg'})  # unpacking to args and kwargs with * and **
# # # func([1, 2, 3], {'site': 'www.softuni.bg'})  # unpacking to args only, without * and **
# # #
# # # ########################################################################################################################
# # #
# # #
# # def func(a, b, c):
# #     print(a, b, c)
# #
# #
# # example_dictionary = {'a': 1, 'b': 2, 'c': 3}
# # func(*example_dictionary)  # ънпакват се ключовете на речника
# # func(**example_dictionary)  # ънпакват се стойностите на речника
# #
# # # Output:
# # # a b c
# # # 1 2 3
# #
# # # ########################################################################################################################
# # '''
# # SORTING
# # '''
# # lst = [5, 4, 1, 2, 3]
# # print(sorted(lst))  # the list remains the same
# #
# # lst.sort()  # the list is permanently sorted in ascending order
# # print(lst)
# #
# #
# # ####
# #
# # lst = ['c', 'a', 'd', 'b']
# #
# # print(sorted(lst, reverse=True))  # first it sorts the list and then prints it backwards
# #
# # ####
# #
# # '''
# # SORTING BY FIRST LETTER
# # '''
# #
# # languages = ['c', 'java', 'python', 'ruby']
# #
# #
# # def select_first_character(word):
# #     return word[0]
# #
# #
# # print(sorted(languages, key=select_first_character))
# # print(sorted(languages, key=lambda word: word[0]))
# #
# #
# #
# # ########################################################################################################################
# # '''
# # Sorting by keys or values
# # '''
# #
# my_dict = {'George': 44, 'Peter': 12, 'John': 28}
#
# print(sorted(my_dict.items(), key=lambda x: x[1]))  # сортира по values
# print(sorted(my_dict.items()))  # сортира по ключове
#
# ########################################################################################################################
#
# '''
# NESTED FUNCTIONS - they cannot be reached from outside main function
# '''
#
#
# def example1():
#     def example2():
#         print('This is nested function')
#     example2()
#
#
# ####
#
#
# def increment_number(number):
#     def nested_increment_number():
#         return number + 1
#     return nested_increment_number()
#
#
# print(increment_number(20))
#
# ####
#
#
# def has_permission(page):
#     def permission(username):
#         if username.lower == 'admin':
#             return f'{username.lower()} has right to open {page}'
#         else:
#             return f'{username} does not have right to open {page}'
#
#     return permission()
#
#
# check_admin_page_permission = has_permission('Admin Page')
# print(check_admin_page_permission('ADMIN'))
#
# ################################## ######################################################################################
#
#
def calculator(operator):
    def addition(a, b):
        return a + b


    def subtraction(a, b):
        return a - b


    def multiplication(a, b):
        return a * b


    def division(a, b):
        if a != 0:
            return a / b
        else:
            return 'Value must be greater than zero'

    if operator == '+':
        return addition

    elif operator == '-':
        return subtraction

    elif operator == '*':
        return multiplication

    elif operator == '/':
        return division


calculator_values = calculator('+')
print(calculator(10, 5))
#
#
# ########################################################################################################################
'''
RECURSION - a function that calls itself
'''


def function(a):
    if 0 < a <= 5:  # ако го няма това условие ще се изпадне в безкраен цикъл
        print(a)
        a += 1
        function(a)


function(1)

####


def countdown(n):
    print(n)

    if n == 0:  # BASE CASE
        return 'end'

    else:
        countdown(n - 1)


countdown(5)

####
'''
FACTORIAL RECURSIVE FUNCTION
'''


def recursion_factorial(n):
    if n == 1:                                  # Това е дъното на рекурсията
        return n

    result = n * recursion_factorial(n - 1)

    print(f"Factorial of ({n}) = {result}")

    return result                               # връща изпълнението на програмата към result


print(recursion_factorial(5))

####

'''
HOW RECURSION WORKS
'''


def function_0():
    print(0)


def function_1():  # преди да се изпълни function_1 се вика function_0
    function_0()
    print(1)


def function_2():  # преди да се изпълни function_2 се вика function_1
    function_1()
    print(2)


def function_3():  # преди да се изпълни function_3 се вика function_2
    function_2()
    print(3)


function_3()
# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
