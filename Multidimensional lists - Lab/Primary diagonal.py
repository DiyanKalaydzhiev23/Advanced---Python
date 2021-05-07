matrix = [input().split() for row in range(int(input()))]
primary_diagonal_sum = 0

for i in range(len(matrix)):
    primary_diagonal_sum += int(matrix[i][i])

print(primary_diagonal_sum)
