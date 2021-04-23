table = set()

for _ in range(int(input())):
    elements = input().split()
    for el in elements:
        table.add(el)

[print(el) for el in table]
