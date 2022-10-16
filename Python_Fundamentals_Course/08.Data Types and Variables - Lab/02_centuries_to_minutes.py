centuries_amount = int(input())
year_is_equal_to = 365.2422

years = centuries_amount * 100
days = int(years * year_is_equal_to)
hours = int(days * 24)
minutes = int(hours * 60)

print(f"{centuries_amount} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
