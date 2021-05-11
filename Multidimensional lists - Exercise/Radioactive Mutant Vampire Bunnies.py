rows, cols = [int(el) for el in input().split()]
matrix = [list(input()) for row in range(rows)]
commands = list(input())
spawn_pos = ((-1, 0), (0, 1), (1, 0), (0, -1))
player_pos = []
dead = False
won = False
result = ""

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "P":
            player_pos = [row, col]


def spread_bunnies():
    global dead, result
    for row in range(rows):
        for column in range(cols):
            if matrix[row][column] == "B":
                for pos in spawn_pos:
                    current_row = row + pos[0]
                    current_col = column + pos[1]
                    if 0 <= current_row < rows and 0 <= current_col < cols:
                        if matrix[current_row][current_col] == ".":
                            matrix[current_row][current_col] = "b"
                        elif matrix[current_row][current_col] == "P" and not won and not dead:
                            dead = True
                            result = f"dead: {current_row} {current_col}"
                            matrix[current_row][current_col] = "b"
    for row in range(rows):
        for column in range(cols):
            if matrix[row][column] == "b":
                matrix[row][column] = "B"
    if won or dead:
        [print(''.join(sublist)) for sublist in matrix]
        print(result)
        raise SystemExit


def move_player(row, column):
    global player_pos, won, dead, result
    if 0 <= row < rows and 0 <= column < cols:
        if matrix[row][column] == "B":
            result = f"dead: {row} {column}"
            matrix[player_pos[0]][player_pos[1]] = "."
            dead = True
        else:
            matrix[player_pos[0]][player_pos[1]] = "."
            player_pos = [row, column]
            matrix[player_pos[0]][player_pos[1]] = "P"
    else:
        result = f"won: {player_pos[0]} {player_pos[1]}"
        matrix[player_pos[0]][player_pos[1]] = "."
        won = True
    spread_bunnies()


while not dead and not won:
    current_command = commands.pop(0)

    if current_command == "U":
        move_player(player_pos[0]-1, player_pos[1])
    elif current_command == "D":
        move_player(player_pos[0]+1, player_pos[1])
    elif current_command == "R":
        move_player(player_pos[0], player_pos[1]+1)
    elif current_command == "L":
        move_player(player_pos[0], player_pos[1]-1)
