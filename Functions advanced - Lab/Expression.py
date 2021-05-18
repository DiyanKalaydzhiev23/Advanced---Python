from itertools import permutations

nums = input().split(", ")
operators = list("+"*len(nums)) + list("-"*len(nums))
operator_combinations = set(permutations(operators, len(nums)))

for comb in operator_combinations:
    expression = ''.join(f"{operator}{num}" for operator, num in list(zip(comb, nums)))
    result = eval(expression)
    print(f"{expression}={result}")
