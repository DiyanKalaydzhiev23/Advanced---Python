def create_triangle(num):
    [print(' '.join([str(n) for n in range(1, r)])) for r in range(2, num+1)]
    [print(' '.join([str(n) for n in range(1, r)])) for r in range(num+1, 1, -1)]

