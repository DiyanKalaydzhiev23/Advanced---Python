from collections import deque

rows, columns = [int(info) for info in input().split()]
snake = list(input())
current_snake = deque(snake.copy())
matrix = []

while len(matrix) < rows:
    current_row = []
    for _ in range(columns):
        if not current_snake:
            current_snake.extend(snake)
        current_row.append(current_snake.popleft())
    if len(matrix) % 2 != 0:
        current_row = current_row[::-1]
    matrix.append(current_row)
    current_snake.extend(snake)

[print("".join(sub_list)) for sub_list in matrix]
