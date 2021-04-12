math_problem = input()
stack = []

for i in range(len(math_problem)):
    if math_problem[i] == "(":
        stack.append(i)
    elif math_problem[i] == ")":
        index = stack.pop()
        print(math_problem[index:i+1])
