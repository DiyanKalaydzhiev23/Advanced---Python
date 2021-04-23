n, m = input().split()
first = set()
second = set()
[first.add(input()) for _ in range(int(n))]
[second.add(input()) for _ in range(int(m))]
common = first.intersection(second)
[print(el) for el in common]
