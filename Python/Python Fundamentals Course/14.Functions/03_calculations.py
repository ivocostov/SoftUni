operation = input()
number_a = int(input())
number_b = int(input())


def multiply():
    return int(number_a * number_b)


def divide():
    return int(number_a / number_b)


def add():
    return int(number_a + number_b)


def subtract():
    return int(number_a - number_b)


if operation == "multiply":
    print(multiply())
elif operation == "divide":
    print(divide())
elif operation == "add":
    print(add())
elif operation == "subtract":
    print(subtract())

