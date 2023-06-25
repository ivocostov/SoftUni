each_employees_happiness = input().split()
happiness_improvement_factor = int(input())

each_employees_happiness = list(map(lambda x: int(x) * happiness_improvement_factor, each_employees_happiness))
filtered_happy_employees = list(filter(lambda x: x >= (sum(each_employees_happiness) / len(each_employees_happiness)), each_employees_happiness))

if len(filtered_happy_employees) >= len(each_employees_happiness) / 2:
    print(f"Score: {len(filtered_happy_employees)}/{len(each_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happy_employees)}/{len(each_employees_happiness)}. Employees are not happy!")
