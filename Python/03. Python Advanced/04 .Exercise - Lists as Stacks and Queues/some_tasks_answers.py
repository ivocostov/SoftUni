# 07 first_way

from collections import deque
from datetime import datetime, timedelta

robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in input().split(";")}  # {name: [time_needed_to_complete_curr_task, time_countdown]
factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)  # timedelta работи с дни, секунди и тн., затова на първата позиция се добавя 0, не работим с дни а със секунди
    product = products.popleft()

# намаляне на времето на робота ако той е зает с някаква задача
    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}  # r[0] - името на робота,
                                                                                               # r[1][0] - нужното време,
                                                                                               # r[1][1] - текущото време за изпълнение - 1 секунда, защото робота
                                                                                               # започва работа една секунда след получаване на задачата

    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(product)
        continue

    robots[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")

# 07 second way

from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(";"):
    name, time_needed = r.split("-")
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1

    for name, value in robots.items():
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")

# 08

from collections import deque

green_window = int(input())
free_window = int(input())
total_cars = 0
cars = deque()
info = input()

while info != "END":
    if info != "green":
        cars.append(info)
    else:
        current_green = green_window

        while current_green > 0 and cars:
            car = cars.popleft()

            time = current_green + free_window

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            current_green -= len(car)
            total_cars += 1

    info = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")