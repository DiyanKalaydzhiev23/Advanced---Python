from collections import deque

parentheses = input()
q = deque()


def not_balanced():
    print("NO")
    raise SystemExit


if not len(parentheses) % 2 == 0:
    not_balanced()


for el in parentheses:
    if el == "(" or el == "[" or el == "{":
        q.append(el)
    else:
        last = q.pop()
        if el == ")":
            if not last == "(":
                not_balanced()
        elif el == "]":
            if not last == "[":
                not_balanced()
        elif el == "}":
            if not last == "{":
                not_balanced()

print("YES")
