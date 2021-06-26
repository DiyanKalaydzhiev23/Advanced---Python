from collections import deque

pizzas = deque([int(n) for n in input().split(", ")])
capacities = deque([int(n) for n in input().split(", ")])
pizzas_made = 0


while pizzas:
    if not capacities:
        print("Not all orders are completed.")
        print(f"Orders left: {', '.join([str(n) for n in pizzas])}")
        raise SystemExit

    pizza = pizzas.popleft()
    capacity = capacities.pop()

    if pizza > 10 or pizza <= 0:
        capacities.append(capacity)
        continue

    if pizza <= capacity:
        pizzas_made += pizza
    else:
        pizzas_made += capacity
        pizzas.appendleft(pizza-capacity)

print("All orders are successfully completed!")
print(f"Total pizzas made: {pizzas_made}")
print(f"Employees: {', '.join([str(n) for n in capacities])}")
