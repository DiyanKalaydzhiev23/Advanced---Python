rows, columns = input().split()
matrix = [input().split() for row in range(int(rows))]
info = input().split()

while info[0] != "END":
    invalid = False

    if len(info) == 5 and info[0] == "swap":
        for i in range(1, 5):
            if i % 2 == 0:
                if not 0 <= int(info[i]) < int(columns):
                    invalid = True
                    break
            else:
                if not 0 <= int(info[i]) <= int(rows):
                    invalid = True
                    break
        if not invalid:
            first = matrix[int(info[1])][int(info[2])]
            second = matrix[int(info[3])][int(info[4])]
            matrix[int(info[1])][int(info[2])] = second
            matrix[int(info[3])][int(info[4])] = first
            [print(*row) for row in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    info = input().split()
