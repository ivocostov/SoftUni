class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.cycles = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cycles += 1

        if self.cycles == self.count:
            raise StopIteration

        return self.step * self.cycles


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
