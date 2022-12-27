number = int(input())

counter = 1
everything_printed = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            everything_printed = True
            break
    if everything_printed:
        break
    print()
