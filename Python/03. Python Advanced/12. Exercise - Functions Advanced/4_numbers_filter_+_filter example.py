def even_odd_filter(**kwargs):
    if 'odd' in kwargs:
        kwargs['odd'] = [n for n in kwargs['odd'] if n % 2 == 1]  # проверява числата и запазва само нечетните

    if 'even' in kwargs:
        kwargs['even'] = list(filter(lambda x: x % 2 == 0, kwargs['even']))  # проверява числата и запазва само четните, прави се на лист, защото иначе е място в паметта


    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))
