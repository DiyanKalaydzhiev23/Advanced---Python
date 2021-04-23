parking = set()

for _ in range(int(input())):
    command, number = input().split(", ")
    if command == "IN":
        parking.add(number)
    else:
        parking.remove(number)

if parking:
    [print(car) for car in parking]
else:
    print("Parking Lot is Empty")
