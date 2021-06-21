from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))

matches = 0
while males and females:
    current_male = males[-1]
    current_female = females[0]

    if current_male <= 0:
        males.pop()
        continue
    elif current_female <= 0:
        females.popleft()
        continue
    elif current_male % 25 == 0:
        males.pop()
        continue
    elif current_female % 25 == 0:
        females.popleft()
        continue
    elif current_male == current_female:
        females.popleft()
        males.pop()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {(', '.join(map(str, reversed(males))))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {(', '.join(map(str, females)))}")
else:
    print(f"Females left: none")