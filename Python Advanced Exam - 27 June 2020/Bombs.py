from collections import deque


def check_bomb():
    if bomb in (40, 60, 120):
        if bomb == 60:
            bombs_dict['Cherry Bombs'] += 1
        elif bomb == 40:
            bombs_dict['Datura Bombs'] += 1
        elif bomb == 120:
            bombs_dict['Smoke Decoy Bombs'] += 1
        return True
    return False


def check_bomb_pouch():
    for bomb_value in bombs_dict.values():
        if bomb_value < 3:
            return False
    return True


bombs_effect = deque(int(n) for n in input().split(", "))
bombs_casings = deque(int(n) for n in input().split(", "))
bombs_dict = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}

while bombs_effect and bombs_casings:
    effect = bombs_effect.popleft()
    casing = bombs_casings.pop()
    bomb = effect + casing
    good_bomb = check_bomb()

    if not good_bomb:
        bombs_casings.append(casing-5)
        bombs_effect.appendleft(effect)

    if check_bomb_pouch():
        break

if check_bomb_pouch():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bombs_effect:
    print(f"Bomb Effects: {', '.join([str(bomb) for bomb in bombs_effect])}")
else:
    print("Bomb Effects: empty")

if bombs_casings:
    print(f"Bomb Casings: {', '.join([str(bomb) for bomb in bombs_casings])}")
else:
    print("Bomb Casings: empty")

for bomb_name, count in bombs_dict.items():
    print(f"{bomb_name}: {count}")
