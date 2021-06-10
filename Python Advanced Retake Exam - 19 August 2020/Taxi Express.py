from collections import deque

customers = deque([int(n) for n in input().split(", ")])
taxis = deque([int(n) for n in input().split(", ")])
total_time = 0


while True:
    customer = customers.popleft()
    taxi = taxis.pop()

    if customer <= taxi:
        total_time += customer
    else:
        customers.appendleft(customer)

    if not customers:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time} minutes")
        break
    if not taxis:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join([str(customer) for customer in customers])}")
        break
