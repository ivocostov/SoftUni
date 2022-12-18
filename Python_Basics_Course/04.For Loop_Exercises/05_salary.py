open_tabs = int(input())
salary = float(input())

for sites in range(open_tabs):
    current_tab = input()
    if current_tab == "Facebook":
        salary -= 150
    elif current_tab == "Instagram":
        salary -= 100
    elif current_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(int(salary))
else:
    print("You have lost your salary.")


