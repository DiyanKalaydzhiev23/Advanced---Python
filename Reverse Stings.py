stack = list(input())
[print(stack.pop(), end="") for _ in range(len(stack))]
