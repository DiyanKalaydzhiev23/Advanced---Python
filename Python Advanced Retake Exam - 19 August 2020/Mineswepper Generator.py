n = int(input())
bombs_mapper = []
matrix = [list("0"*n) for row in range(n)]
directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

for bomb in range(int(input())):
    x, y = input().split(", ")
    bombs_mapper.append((int(x[1:]), int(y[0:-1])))

for row in range(n):
    for col in range(n):
        if (row, col) in bombs_mapper:
            matrix[row][col] = "*"
            for direction in directions:
                current_row = row + direction[0]
                current_col = col + direction[1]
                if 0 <= current_row < n and 0 <= current_col < n:
                    if matrix[current_row][current_col] != "*":
                        number = int(matrix[current_row][current_col])
                        number += 1
                        matrix[current_row][current_col] = number

[print(' '.join([str(el) for el in row])) for row in matrix]
