def cache(func):  # ** def fibonacci(n) **
                            # речника, ако не трябва да се закачи като атрибут на функцията се прави тук в ** cache **,
                            # защото иначе ако се сложи в wrapper ще се занулява всеки път,
                            # тъй като на всяка итерация ще се извиква wrapper и речника ще се занулява

    def wrapper(num):
        if num not in wrapper.log:
            wrapper.log[num] = func(num)    # ако в речника го няма ключа, то връщаме процеса към ** def fibonacci(n) **
                                            # за да се пресметне стойността към ключа
        return wrapper.log[num]

    wrapper.log = {}        # по този начин речника се закача като атрибут на функцията

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    else:                                               # Първо се връща от fibonacci(n - 1) и се праща на ** def wrapper(num) ** и така до 0. (3, 2, 1, 0)
        return fibonacci(n - 1) + fibonacci(n - 2)      # И 1 и 0 са по малки от две така че се запазват в речника.
                                                        # Като стигне до нула се връща от fibonacci(n - 2)


fibonacci(3)                # {1: 1, 0: 0, 2: 1, 3: 2}
print(fibonacci.log)        #


fibonacci(4)                # {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
print(fibonacci.log)        #
