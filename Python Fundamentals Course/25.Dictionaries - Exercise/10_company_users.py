<<<<<<< HEAD
companies_dictionary = {}

while True:
    command = input()
    if command == 'End':
        break

    company, id = command.split(" -> ")

    if company not in companies_dictionary.keys():
        companies_dictionary[company] = []
    if id not in companies_dictionary[company]:
        companies_dictionary[company].append(id)

for company_name, employee_id in companies_dictionary.items():
    print(company_name)
    employee_id = '\n'.join(f"-- {employee_id}" for employee_id in companies_dictionary[company_name])
    print(employee_id)
=======
companies_dictionary = {}

while True:
    command = input()
    if command == 'End':
        break

    company, id = command.split(" -> ")

    if company not in companies_dictionary.keys():
        companies_dictionary[company] = []
    if id not in companies_dictionary[company]:
        companies_dictionary[company].append(id)

for company_name, employee_id in companies_dictionary.items():
    print(company_name)
    employee_id = '\n'.join(f"-- {employee_id}" for employee_id in companies_dictionary[company_name])
    print(employee_id)
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
