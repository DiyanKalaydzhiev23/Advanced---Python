text = list(input())
n = int(input())
matrix = [list(input()) for _ in range(n)]
commands = [input() for _ in range(int(input()))]
movement = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
player_pos = [0, 0]

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "P":
            player_pos = [row, col]
            break

for i in range(len(commands)):
    command = commands[i]
    row, col = movement[command]
    current_row = player_pos[0] + row
    current_col = player_pos[1] + col
    if 0 <= current_row < n and 0 <= current_col < n:
        if matrix[current_row][current_col] != "-":
            text.append(matrix[current_row][current_col])
        matrix[player_pos[0]][player_pos[1]] = "-"
        matrix[current_row][current_col] = "P"
        player_pos = [current_row, current_col]
    else:
        if text:
            text.pop()

print(''.join(text))
[print(''.join(row)) for row in matrix]
