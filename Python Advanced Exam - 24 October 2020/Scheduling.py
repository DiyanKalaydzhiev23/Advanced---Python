from sys import maxsize

tasks = [int(n) for n in input().split(", ")]
priority_task = int(input())
cycles = 0
fastest_task_i = None
tasks_done = []


def find_task():
    smallest_task = maxsize
    smallest_task_i = None

    for i in range(len(tasks)):
        if i not in tasks_done:
            if tasks[i] < smallest_task:
                smallest_task = tasks[i]
                smallest_task_i = i

    return smallest_task_i


while fastest_task_i != priority_task:
    fastest_task_i = find_task()
    task = tasks[fastest_task_i]
    cycles += task
    tasks_done.append(fastest_task_i)

print(cycles)
