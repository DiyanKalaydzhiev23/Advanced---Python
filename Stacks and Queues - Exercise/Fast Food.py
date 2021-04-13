from collections import deque

storage = int(input())
clients = deque([int(el) for el in input().split()])
print(max(clients))

for _ in range(len(clients)):
    if storage <= 0:
        break
    elif clients[0] <= storage:
        storage -= clients[0]
        clients.popleft()

if clients:
    print(f"Orders left: {' '.join([str(el) for el in clients])}")
else:
    print("Orders complete")
