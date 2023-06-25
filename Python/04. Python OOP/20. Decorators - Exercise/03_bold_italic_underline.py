def make_bold(func):
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"  # извикай функцията която се декорира с аргументите които тя има

    return wrapper


def make_italic(func):
    def wrapper(*args):
        return f"<i>{func(*args)}</i>"  # извикай функцията която се декорира с аргументите които тя има

    return wrapper


def make_underline(func):
    def wrapper(*args):
        return f"<u>{func(*args)}</u>"  # извикай функцията която се декорира с аргументите които тя има

    return wrapper


@make_bold                  # декорира @make_italic
@make_italic                # декорира се от @make_bold и декорира @make_underline
@make_underline             # декорира се от @make_italic и декорира ** def greet(name) **
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))       # извиква се wrapper na ** def make_underline(func) **, след това ---//--- на ** def make_italic(func): **,
                            # след това ---//--- на ** def make_bold(func): **, като след това всеки декоратор си връща резултата


# @make_bold
# @make_italic
# @make_underline
# def greet_all(*args):
#     return f"Hello, {', '.join(args)}"
#
# print(greet_all("Peter", "George"))
