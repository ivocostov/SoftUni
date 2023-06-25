from itertools import permutations
from typing import List


def possible_permutations(numbers: List[int]):
    for nums in permutations(numbers):
        yield nums




[print(n) for n in possible_permutations([1])]
[print(n) for n in possible_permutations([1, 2, 3])]