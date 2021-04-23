numbers = tuple(map(float, input().split()))
already_calculated = []

for n in numbers:
    if n not in already_calculated:
        already_calculated.append(n)
        print(f"{n} - {numbers.count(n)} times")
