from collections import deque

green_duration = int(input())
free_window = int(input())
total_cars = 0
cars = deque()
info = input()

while info != "END":
    if info != "green":
        cars.append(info)
    else:
        current_green = green_duration
        while current_green > 0:
            if not cars:
                break
            car = cars.popleft()
            if len(car) > current_green:
                if len(car) > current_green + free_window:
                    hit_at = car[current_green + free_window]
                    print(f"A crash happened!\n{car} was hit at {hit_at}.")
                    raise SystemExit
            current_green -= len(car)
            total_cars += 1
    info = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
