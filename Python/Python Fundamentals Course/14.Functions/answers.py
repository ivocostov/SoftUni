# basic calculator
def intro():
    return '''##################################
# Welcome to SoftUni Calculator  #
#   Please select an option to   #
#          continue              #
#                                #
#                                #
#   Author: Mario Zahariev       #
#   Course: SoftUni Fundamentals #
#                                #
##################################\n'''


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(intro())

while True:
    choice = input('1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\nEnter your choice: ')

    if choice == '5':
        print('Thank you for using our calculator!!!')
        break

    if choice == '1':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print('The sum is: ', add(n1, n2), '\n')

    elif choice == '2':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print('The result of the subtract is: ', subtract(n1, n2), '\n')

    elif choice == '3':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print('The sum is: ', multiply(n1, n2), '\n')

    elif choice == '4':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print('The sum is: ', divide(n1, n2), '\n')

    else:
        print('Wrong choice!!!\n')

# 1.	Absolute Values
numbers = input().split(' ')
abs_numbers = []

for num in numbers:
    abs_numbers.append(abs(float(num)))

print(abs_numbers)


# numbers = list(map(float, input().split(' ')))
# result = [abs(num) for num in numbers]
# print(result)

# 2.	Grades
def type_of_grade(score):
    if 2.00 <= score <= 2.99:
        return 'Fail'
    elif 3.00 <= score <= 3.49:
        return "Poor"
    elif 3.50 <= score <= 4.49:
        return "Good"
    elif 4.50 <= score <= 5.49:
        return "Very Good"
    elif 5.50 <= score <= 6.00:
        return "Excellent"


score = float(input())
print(type_of_grade(score))


# 3.	Calculations
def calculation_func(number_a, number_b, operation):
    if operation == "multiply":
        return number_a * number_b

    elif operation == "divide":
        return int(number_a / number_b)

    elif operation == "add":
        return number_a + number_b

    elif operation == "subtract":
        return number_a - number_b


type_of_operation = input()
first_number = int(input())
second_number = int(input())
print(calculation_func(first_number, second_number, type_of_operation))

# 4.	Repeat String
string = input()
number = int(input())
result = lambda string, num: string * num
print(result(string, number))

# 7.	Rounding
result = list(map(lambda x: round(float(x)), input().split(' ')))

print(result)