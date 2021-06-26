players = input().split(", ")
board = [input().split() for _ in range(7)]
scores = [501, 501]
throws = [0, 0]
indexes = [0, 1]


def letter_points(rows, cols, multiplayer):
    left = int(board[rows][0])
    right = int(board[rows][-1])
    up = int(board[0][cols])
    down = int(board[-1][cols])
    total = (up + down + left + right) * multiplayer
    return total


while scores[0] > 0 and scores[1] > 0:
    row, col = input().lstrip("(").rstrip(")").split(", ")
    row = int(row)
    col = int(col)
    player = indexes.pop(0)
    throws[player] += 1

    if 0 <= row < 7 and 0 <= col < 7:
        el = board[row][col]
        if el.isdigit():
            scores[player] -= int(el)
        elif el == "D":
            scores[player] -= letter_points(row, col, 2)
        elif el == "T":
            scores[player] -= letter_points(row, col, 3)
        elif el == "B":
            print(f"{players[player]} won the game with {throws[player]} throws!")
            raise SystemExit

    indexes.append(player)

for i in range(2):
    if scores[i] <= 0:
        print(f"{players[i]} won the game with {throws[i]} throws!")
