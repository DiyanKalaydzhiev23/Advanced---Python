even_set = set()
odd_set = set()


for row in range(int(input())):
    name = input()
    ascii_letters = [ord(letter) for letter in name]
    result = sum(ascii_letters) // (row+1)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(even_set) == sum(odd_set):
    [odd_set.add(n) for n in even_set]
elif sum(even_set) < sum(odd_set):
    odd_set = odd_set.difference(even_set)
else:
    odd_set = odd_set.symmetric_difference(even_set)

print(', '.join([str(n) for n in odd_set]))
