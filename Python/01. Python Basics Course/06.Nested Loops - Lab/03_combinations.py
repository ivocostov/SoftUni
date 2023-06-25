number = int(input())
possible_solutions = 0

# x1 + x2 + x3 = n
for x1 in range(0, number + 1):
    for x2 in range(0, number + 1):
        for x3 in range(0, number + 1):
            if x1 + x2 + x3 == number:
                possible_solutions += 1
print(f"{possible_solutions}")
