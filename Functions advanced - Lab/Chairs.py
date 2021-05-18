from itertools import combinations


names = list(input().split(", "))
n = int(input())
[print(', '.join(comb)) for comb in combinations(names, n)]
