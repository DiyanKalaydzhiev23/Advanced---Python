def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for _ in range(2, n):
        row = [1]
        last_row = triangle[-1]
        for i in range(1, len(last_row)):
            num = last_row[i-1] + last_row[i]
            row.append(num)
        row.append(1)
        triangle.append(row)

    return triangle


get_magic_triangle(5)
