from collections import deque

n = int(input())
commands = deque(input().split())
road = [input().split() for _ in range(n)]
miner_pos = []
collected_coal = 0
total_coal = 0

for row in range(n):
    for col in range(n):
        if road[row][col] == "s":
            miner_pos = [row, col]
        elif road[row][col] == "c":
            total_coal += 1


def move(rows, cols):
    global collected_coal, miner_pos
    road[miner_pos[0]][miner_pos[1]] = "*"
    if road[rows][cols] == "c":
        collected_coal += 1
    elif road[rows][cols] == "e":
        print(f"Game over! ({rows}, {cols})")
        raise SystemExit
    miner_pos = [rows, cols]
    if collected_coal == total_coal:
        print(f"You collected all coals! ({rows}, {cols})")
        raise SystemExit


while commands:
    current_command = commands.popleft()
    if current_command == "up":
        if 0 <= miner_pos[0]-1 < n:
            move(miner_pos[0]-1, miner_pos[1])
    elif current_command == "down":
        if 0 <= miner_pos[0]+1 < n:
            move(miner_pos[0]+1, miner_pos[1])
    elif current_command == "right":
        if 0 <= miner_pos[1]+1 < n:
            move(miner_pos[0], miner_pos[1]+1)
    elif current_command == "left":
        if 0 <= miner_pos[1]-1 < n:
            move(miner_pos[0], miner_pos[1]-1)

print(f"{total_coal-collected_coal} coals left. ({miner_pos[0]}, {miner_pos[1]})")
