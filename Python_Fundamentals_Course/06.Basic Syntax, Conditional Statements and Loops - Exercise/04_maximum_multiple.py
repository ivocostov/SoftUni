divisor = int(input())
boundary = int(input())

for current_number in range(boundary, -1, -1):
    if current_number % divisor == 0:
        print(current_number)
        break
