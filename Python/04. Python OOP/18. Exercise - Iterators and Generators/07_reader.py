def read_next(*args):
    for element in args:
        for sub_el in element:
            yield sub_el


# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
