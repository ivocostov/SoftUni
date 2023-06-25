<<<<<<< HEAD
import re

dates = input()

searched_pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'
valid_dates = re.findall(searched_pattern, dates)

for date in valid_dates:
=======
import re

dates = input()

searched_pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'
valid_dates = re.findall(searched_pattern, dates)

for date in valid_dates:
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")