def solution():

    def integers():
        """ Създава се безкраен брой integers по условие започващи от 1 """
        num = 1

        while True:
            yield num
            num += 1

    def halves():
        """ Изчислява се половинката на всяко число генерирано в def integers() """
        for i in integers():
            yield i / 2

    def take(n, seq):
        """ Връща n на брой числа от seq ( като seq в случая приема за референция някоя от горните функции )"""
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

