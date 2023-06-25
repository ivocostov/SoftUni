import math
from typing import List


def get_primes(numbers: List[int]):  # receive a list of integer numbers
    for number in numbers:
        if number <= 1:  # if number is equal or less than 1, obviously it's not prime ( primes are divided only to themselves and 1 )
            continue

        for num in range(2, int(math.sqrt(number)) + 1):  # if sqrt of a number divide without remains it's not prime
            if number % num == 0:
                break

        else:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))