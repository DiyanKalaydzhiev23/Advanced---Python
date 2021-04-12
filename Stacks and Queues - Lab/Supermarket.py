from collections import deque

command = input()
q = deque()

while command != "End":
    if command == "Paid":
        while q:
            print(q.popleft())
    else:
        q.append(command)
    command = input()

print(f"{len(q)} people remaining.")
