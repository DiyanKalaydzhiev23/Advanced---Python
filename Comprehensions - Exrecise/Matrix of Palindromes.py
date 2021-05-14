rows, cols = [int(n) for n in input().split()]
matrix = [[f"{chr(97+row)}{chr(97+row+col)}{chr(97+row)}" for col in range(cols)] for row in range(rows)]
[print(*row) for row in matrix]
