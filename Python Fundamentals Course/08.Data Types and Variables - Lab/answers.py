# 2 Convert Meters to Kilometers
meters = int(input())
kilometers = meters / 1000
print(f'{kilometers:.2f}')

# 3 Pounds to Dollars
from forex_python.converter import CurrencyRates

amount = int(input('Amount in GBP: '))
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
result = amount * current_rate
print(f'{amount} GBP is {result:.3f} USD')

# 4 Centuries to Minutes
century = int(input())
years = century * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f'{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')

# 6 Next happy year
year = int(input())
happy_year_condition = False

while not happy_year_condition:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year_condition = len(set_year) == len(str(year))

print(year)

from itertools import permutations

number = tuple(map(int, input()))
myperm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))

for digits in list(myperm):
    if digits > number:
        result = ''.join(str(x) for x in digits)
        print(result)
        break