from collections import deque
circle = deque([input().split() for _ in range(int(input()))])
found = False
index = 0
petrol = 0

while not found:
    found = True
    current_circle = circle.copy()
    for i in range(len(circle)):
        tokens = current_circle.popleft()
        refill, dist = int(tokens[0]), int(tokens[-1])
        petrol += refill - dist
        if petrol < 0:
            found = False
            petrol = 0
            index += 1
            circle.append(circle.popleft())
            break

print(index)
