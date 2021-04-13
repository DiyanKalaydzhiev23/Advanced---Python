numbers = input().split(" ")
[print(numbers.pop(), end=" ") for _ in range(len(numbers))]
