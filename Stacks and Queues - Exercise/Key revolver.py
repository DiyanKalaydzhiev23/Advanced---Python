from collections import deque

bullet_price = int(input())
mag_max = int(input())
bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])
reward = int(input())
mag = mag_max
bullets_shot = 0

while True:
    if not bullets:
        if locks:
            print(f"Couldn't get through. Locks left: {len(locks)}")
        else:
            print(f"0 bullets left. Earned ${reward-bullets_shot*bullet_price}")
        break
    elif not locks:
        print(f"{len(bullets)} bullets left. Earned ${reward-bullets_shot*bullet_price}")
        break
    bullet = bullets.pop()
    lock = locks.popleft()
    bullets_shot += 1
    mag -= 1
    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)
    if mag == 0:
        if bullets:
            if len(bullets) > mag_max:
                mag = mag_max
            else:
                mag = len(bullets)
            print("Reloading!")
