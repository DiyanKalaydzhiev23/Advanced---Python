from sys import maxsize

rows, columns = input().split()
matrix = [[int(n) for n in input().split()] for row in range(int(rows))]
max_sum = -maxsize
biggest_matrix = []

for row in range(int(rows)-2):
    for i in range(int(columns)-2):
        first_row = matrix[row][i:i+3]
        second_row = matrix[row+1][i:i+3]
        third_row = matrix[row+2][i:i+3]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix.clear()
            biggest_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*biggest_matrix[row]) for row in range(3)]
