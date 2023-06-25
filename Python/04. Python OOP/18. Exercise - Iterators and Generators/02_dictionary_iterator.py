from typing import Dict


class dictionary_iter:
    def __init__(self, dictionary: Dict):
        self.dictionary = list(dictionary.items())
        self.dict_length = len(dictionary)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.dict_length - 1:
            raise StopIteration

        self.index += 1
        return self.dictionary[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
