names = input().split(", ")
data = {name: [[], []] for name in names}
command = input()

while command != "End":
    name, item, cost = command.split("-")

    if item not in data[name][0]:
        data[name][0].append(item)
        data[name][1].append(int(cost))

    command = input()

[print(f"{name} -> Items: {len(data[name][0])}, Cost: {sum(data[name][1])}") for name in data]
