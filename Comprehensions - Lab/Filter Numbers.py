start = int(input())
end = int(input())
result = {n for n in range(start, end+1) for num in range(2, 11) if n % num == 0}
print(list(result))
