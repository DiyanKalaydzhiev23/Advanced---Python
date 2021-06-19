board = [input().split() for row in range(8)]
moves = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
k_pos = []
queens = []

for row in range(8):
    for col in range(8):
        if board[row][col] == "K":
            k_pos = [row, col]

for move in moves:
    row, col = k_pos
    move_row, move_col = move
    while True:
        row += move_row
        col += move_col
        if 0 <= row < 8 and 0 <= col < 8:
            if board[row][col] == "Q":
                queens.append([row, col])
                break
        else:
            break

if queens:
    [print(queen) for queen in queens]
else:
    print("The king is safe!")
