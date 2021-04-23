info = input().split("-")
phone_book = {}

while not info[0].isdigit():
    phone_book[info[0]] = info[1]
    info = input().split("-")

for _ in range(int(info[0])):
    name = input()
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")