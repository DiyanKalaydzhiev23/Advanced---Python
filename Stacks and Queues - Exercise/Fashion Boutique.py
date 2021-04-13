stack = [int(el) for el in input().split()]
capacity = int(input())
total_racks = 1
current_rack = 0

while stack:
    if current_rack + stack[-1] <= capacity:
        current_rack += stack.pop()
    else:
        total_racks += 1
        current_rack = 0

print(total_racks)
