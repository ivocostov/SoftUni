# companies = {'Sony': 120, 'Apple': 150, 'Samsung': 105, 'Hp': 132, 'Acer': 125}
#
#
# sorted_companies_data = sorted(companies.items(), key=lambda x: x[1])  # сортира във възходящ ред по values
#
# sorted_companies_data = sorted(companies.items(), key=lambda x: x[0])  # сортира във възходящ ред по keys



########################################################################################################################



companies = {'Sony': 120, 'Apple': 150, 'Samsung': 105, 'Hp': 132, 'Acer': 125, 'Acea': 125}  # Acea би трябвало да дойде преди Аcer след сортирането

sorted_companies_data = sorted(companies.items(), key=lambda x: (x[1], x[0]))  # сортира първо във възходящ ред по keys и след това във възходящ ред по values

sorted_data = sorted(healing_items.items(), key=lambda x: (-x[1], x[0])) # сортира първо във низходящ ред по values и след това във възходящ ред по keys


