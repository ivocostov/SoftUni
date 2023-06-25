class vowels:
    def __init__(self, string: str):
        self.string = string

    def __iter__(self):
        return self

    def __next__(self):
        