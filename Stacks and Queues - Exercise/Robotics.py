from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
robots = {}
products = deque()
time = datetime.strptime(input(), "%H:%M:%S") + timedelta(seconds=1)
product = input()

for info in data:
    info = info.split("-")
    robots[info[0]] = [int(info[1]), time]

free_robots = deque(robots)

while product != "End":
    products.append(product)
    product = input()

while products:
    current_product = products.popleft()
    if free_robots:
        robot = free_robots.popleft()
        robots[robot][1] = time + timedelta(seconds=robots[robot][0])
        print(f"{robot} - {current_product} [{time.strftime('%H:%M:%S')}]")
        for r in robots:
            if r not in free_robots:
                if time + timedelta(seconds=1) >= robots[r][1]:
                    free_robots.append(r)
    else:
        for r in robots:
            if time + timedelta(seconds=1) >= robots[r][1]:
                free_robots.append(r)
        products.append(current_product)
    time += timedelta(seconds=1)
