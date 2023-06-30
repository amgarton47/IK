import json

f = open("1.txt")
data = json.load(f)["matrix"]
f.close()


def number_of_paths(matrix):
    m, n = len(matrix[0]), len(matrix)
    print(m)

    if n == 1:
        return 0 if 0 in matrix[0] else 1

    if m == 1:
        for row in matrix:
            if row[0] == 0:
                return 0

        return 1

    table = [[0 for _ in range(m)] for _ in range(n)]
    table[0][0] = matrix[0][0]

    for i in range(1, m):
        if matrix[0][i] == 1:
            table[0][i] = table[0][i - 1]
        else:
            table[0][i] = 0

    for i in range(1, n):
        if matrix[i][0] == 1:
            table[i][0] = table[i - 1][0]
        else:
            table[i][0] = 0

    if matrix[0][0] == 0:
        return 0

    for row in range(1, n):
        for col in range(1, m):
            if matrix[row][col] == 1:
                table[row][col] = table[row - 1][col] + table[row][col - 1] % 1000000007
            else:
                matrix[row][col] = 0

    return table[n - 1][m - 1] % 1000000007


input = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
input = [[1, 1], [0, 1]]
input = [[1, 1, 0]]
input = data

print(number_of_paths(input))
