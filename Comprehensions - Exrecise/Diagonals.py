n = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[n-i-1][i] for i in range(n-1, -1, -1)]
print(f"First diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}")
