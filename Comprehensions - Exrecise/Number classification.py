numbers = [int(n) for n in input().split(", ")]
print(f"Positive: {', '.join([str(n) for n in numbers if n >= 0])}")
print(f"Negative: {', '.join([str(n) for n in numbers if n < 0])}")
print(f"Even: {', '.join([str(n) for n in numbers if n % 2 == 0])}")
print(f" Odd: {', '.join([str(n) for n in numbers if n % 2 != 0])}")
