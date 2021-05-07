rows, columns = input().split(", ")
matrix = [[int(n) for n in input().split(", ")] for row in range(int(rows))]
biggest_square = []
square_sum = 0

for row in range(len(matrix)-1):
    for i in range(int(columns)-1):
        first_row = [matrix[row][i], matrix[row][i+1]]
        second_row = [matrix[row+1][i], matrix[row+1][i+1]]
        current_sum = sum(first_row) + sum(second_row)
        if current_sum > square_sum:
            biggest_square.clear()
            biggest_square.append(first_row)
            biggest_square.append(second_row)
            square_sum = current_sum

[print(*biggest_square[row]) for row in range(2)]
print(square_sum)
