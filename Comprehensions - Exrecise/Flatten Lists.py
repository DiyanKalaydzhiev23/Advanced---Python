strings = input().split("|")
numbers = [[n for n in string.split()] for string in strings]
print(' '.join([' '.join(string) for string in numbers[::-1] if string]))
