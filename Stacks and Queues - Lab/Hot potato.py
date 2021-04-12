from collections import deque
q = deque(input().split())
n = int(input())

while len(q) > 1:
    for _ in range(n):
        q.append(q.popleft())
    print(f"Removed {q.pop()}")

print(f"Last is {''.join(q)}")
