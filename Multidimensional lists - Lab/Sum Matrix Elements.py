rows, columns = input().split(", ")
matrix = []
sum_matrix = 0

for row in range(int(rows)):
    info = [int(x) for x in input().split(", ")]
    matrix.append(info)
    sum_matrix += sum(info)

print(sum_matrix)
print(matrix)
