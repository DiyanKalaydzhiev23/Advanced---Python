matrix = [list(input()) for row in range(int(input()))]
symbol = input()

for row in range(len(matrix)):
    for i in range(len(matrix)):
        if matrix[row][i] == symbol:
            print((row, i))
            raise SystemExit

print(f"{symbol} does not occur in the matrix")
