def repeat_n_times(func):       # hello ще се запише в декоратор функцията като IDE-то ще мине през декоратор функцията само веднъж
    def wrapper(*args):         # след това се извиква всеки път на изпълнение wrapper
        func(*args)

    return wrapper



@repeat_n_times                 #  може да се напише и @repeat_n_times(5), Което означава че функцията hello ще се изпълни 5 пъти
def hello(name):
    print(f'Hello {name}')


hello('Alice')                 # когато се извиква функция hello се изпълнява директно ** def wrapper **


# ----------------------------------------------------------------------------------------------------------------------

""" Ако се направи по този начин по-долу """


def repeat_n_times(n):              # ** def repeat_n_times(n) ** ще приема някакво число, което се задава така: @repeat_n_times(5)
    def decorator(func):            # а hello ще се запише в ** def decorator ** функцията
        def wrapper(*args):         # след това пак се извиква всеки път на изпълнение wrapper
            func(*args)

        return wrapper

    return decorator


@repeat_n_times                     #  може да се напише и @repeat_n_times(5), Което означава че функцията hello ще се изпълни 5 пъти
def hello(name):                    # ако над @repeat_n_times(5) се напише още веднъж @repeat_n_times(2) функцията ще се изпълни 10 пъти
    print(f'Hello {name}')          # т.е. два пъти извикваме функцията с по 5 изпълнения


hello('Alice')


########################################################################################################################