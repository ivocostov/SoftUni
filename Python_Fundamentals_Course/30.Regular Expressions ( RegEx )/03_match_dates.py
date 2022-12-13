import re

dates = input()

searched_pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'
valid_dates = re.findall(searched_pattern, dates)

for date in valid_dates:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")