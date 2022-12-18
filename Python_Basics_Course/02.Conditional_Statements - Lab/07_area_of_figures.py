from math import pi
figure = input()
area = 0

if figure == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")

elif figure == "circle":
    r = float(input())
    area = (r**2) * pi
    print(f"{area:.3f}")

elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = 1/2 * a * h
    print(f"{area:.3f}")
