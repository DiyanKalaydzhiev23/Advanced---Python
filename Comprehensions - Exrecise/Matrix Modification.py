n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
data = input()

while data != "END":
    command, row, col, value = data.split()

    if command == "Add":
        if 0 <= int(row) < n and 0 <= int(col) < n:
            matrix[int(row)][int(col)] += int(value)
        else:
            print("Invalid coordinates")
    elif command == "Subtract":
        if 0 <= int(row) < n and 0 <= int(col) < n:
            matrix[int(row)][int(col)] -= int(value)
        else:
            print("Invalid coordinates")

    data = input()

[print(*nums) for nums in matrix]
