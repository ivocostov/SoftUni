numbers = int(input())
counter = 0
current_number = 0
counter_p1 = 0
counter_p2 = 0
counter_p3 = 0
counter_p4 = 0
counter_p5 = 0

for num in range(1, numbers + 1):
    current_number = int(input())
    counter = counter + 1
    if current_number < 200:
        counter_p1 = counter_p1 + 1
    elif 200 <= current_number <= 399:
        counter_p2 = counter_p2 + 1
    elif 400 <= current_number <= 599:
        counter_p3 = counter_p3 + 1
    elif 600 <= current_number <= 799:
        counter_p4 = counter_p4 + 1
    else:
        counter_p5 = counter_p5 + 1

p1 = counter_p1 / counter * 100
p2 = counter_p2 / counter * 100
p3 = counter_p3 / counter * 100
p4 = counter_p4 / counter * 100
p5 = counter_p5 / counter * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

