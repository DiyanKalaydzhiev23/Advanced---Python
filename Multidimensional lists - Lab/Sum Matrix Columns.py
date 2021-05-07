rows, columns = input().split(", ")
matrix = [[int(n) for n in input().split()] for row in range(int(rows))]

for i in range(int(columns)):
    column_sum = 0
    for row in matrix:
        column_sum += row[i]
    print(column_sum)
