n = int(input())
matrix = [list(input()) for _ in range(n)]
positions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, 1), (2, -1), (1, 2), (1, -2))
removed_knights = 0

while True:
    max_kills = 0
    max_killer = []
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                kills = 0
                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]
                    if 0 <= pos_row < n and 0 <= pos_col < n:
                        if matrix[pos_row][pos_col] == "K":
                            kills += 1
                if kills > max_kills:
                    max_killer = [row, col]
                    max_kills = kills
    if max_killer:
        matrix[max_killer[0]][max_killer[1]] = "0"
        removed_knights += 1
    else:
        print(removed_knights)
        raise SystemExit
