longest = []

for _ in range(int(input())):
    info = input().split("-")
    first = info[0].split(",")
    second = info[1].split(",")
    first_set = set(n for n in range(int(first[0]), int(first[1])+1))
    second_set = set(n for n in range(int(second[0]), int(second[1])+1))
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest):
        longest = list(intersection)

print(f"Longest intersection is {longest} with length {len(longest)}")
