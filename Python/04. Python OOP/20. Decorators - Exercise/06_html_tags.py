def tags(html_tag):
    def decorator(func):
        def wrapper(*args):
            result = f'<{html_tag}>{func(*args)}</{html_tag}>'
            return result
        return wrapper
    return decorator


#
# @tags('p')                                  # <p>Hello you!</p>
# def join_strings(*args):
#     return "".join(args)


# print(join_strings("Hello", " you!"))

#-----------------------------------------------------------------------------------

@tags('h1')                               # <h1>HELLO</h1>
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
