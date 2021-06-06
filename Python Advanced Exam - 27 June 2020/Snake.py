n = int(input())
road = [list(input()) for _ in range(n)]
navigation = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}


def find_snake():
    for row in range(n):
        for col in range(n):
            if road[row][col] == "S":
                return [row, col]


def find_other_portal():
    for row in range(n):
        for col in range(n):
            if road[row][col] == "B":
                return [row, col]


snake = find_snake()
food = 0

while True:
    road[snake[0]][snake[1]] = "."
    command_pos = navigation[input()]
    snake[0] += command_pos[0]
    snake[1] += command_pos[1]

    if not (0 <= snake[0] < n and 0 <= snake[1] < n):
        print("Game over!")
        break

    if road[snake[0]][snake[1]] == "B":
        road[snake[0]][snake[1]] = "."
        snake = find_other_portal()
    elif road[snake[0]][snake[1]] == "*":
        food += 1
    road[snake[0]][snake[1]] = "S"

    if food == 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food}")
[print(''.join(row)) for row in road]
