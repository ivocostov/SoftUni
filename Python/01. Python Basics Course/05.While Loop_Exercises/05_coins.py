sum_taken = float(input())
sum_taken = int(sum_taken * 100)
coins_counter = 0

while sum_taken > 0:
    if sum_taken - 200 >= 0:
        coins_counter += 1
        sum_taken -= 200
    elif sum_taken - 100 >= 0:
        coins_counter += 1
        sum_taken -= 100
    elif sum_taken - 50 >= 0:
        coins_counter += 1
        sum_taken -= 50
    elif sum_taken - 20 >= 0:
        coins_counter += 1
        sum_taken -= 20
    elif sum_taken - 10 >= 0:
        coins_counter += 1
        sum_taken -= 10
    elif sum_taken - 5 >= 0:
        coins_counter += 1
        sum_taken -= 5
    elif sum_taken - 2 >= 0:
        coins_counter += 1
        sum_taken -= 2
    elif sum_taken - 1 >= 0:
        coins_counter += 1
        sum_taken -= 1
print(coins_counter)
