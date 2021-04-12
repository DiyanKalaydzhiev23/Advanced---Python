from collections import deque

water = int(input())
q = deque()
name = input()

while name != "Start":
    q.append(name)
    name = input()

command = input().split()

while command[0] != "End":
    if command[0] == "refill":
        water += int(command[1])
    else:
        if int(command[0]) <= water:
            water -= int(command[0])
            print(f"{q.popleft()} got water")
        else:
            print(f"{q.popleft()} must wait")
    command = input().split()

print(f"{water} liters left")
