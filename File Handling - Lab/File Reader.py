with open("Files/numbers.txt", "r") as number_file:
    numbers = number_file.readlines()

print(sum([int(n[::-1]) for n in numbers]))
