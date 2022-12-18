n1 = int(input())
n2 = int(input())
operator = input()

if operator == '+':
    result = n1 + n2
    odd_check = result % 2 == 0
    if odd_check is True:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == '-':
    result = n1 - n2
    odd_check = result % 2 == 0
    if odd_check is True:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == '*' and n1 != 0 and n2 != 0:
    result = n1 * n2
    odd_check = result % 2 == 0
    if odd_check is True:
        print(f"{n1} {operator} {n2} = {result} - even")
    elif odd_check is False:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == '/':
    if n1 == 0:
        print(f"Cannot divide {n2} by zero")
    elif n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {operator} {n2} = {result:.2f}")

elif operator == '%':
    if n1 == 0:
        print(f"Cannot divide {n2} by zero")
    elif n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {operator} {n2} = {result}")

