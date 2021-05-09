n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
coordinates = [info.split(",") for info in input().split()]
explode_positions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))  # 0 index is the row, 1 index is the column
alive_count = 0
alive_cells_sum = 0

for coordinate in coordinates:
    row = int(coordinate[0])
    col = int(coordinate[1])
    value = matrix[row][col]
    if value > 0:
        matrix[row][col] = 0
        for pos in explode_positions:
            current_row = row + pos[0]
            current_col = col + pos[1]
            if 0 <= current_row < n and 0 <= current_col < n:
                if matrix[current_row][current_col] > 0:
                    matrix[current_row][current_col] -= value

for row in matrix:
    for el in row:
        if el > 0:
            alive_count += 1
            alive_cells_sum += el

print(f"Alive cells: {alive_count}\nSum: {alive_cells_sum}")
[print(*sub_list) for sub_list in matrix]
