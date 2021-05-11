matrix = [[int(el) for el in input().split(", ")] for _ in range(int(input()))]
print([[n for n in row if n % 2 == 0] for row in matrix])
