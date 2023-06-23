def count_islands(matrix):
    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (-1, 1),
        (1, -1),
        (-1, -1),
        (1, 1),
    ]

    n = len(matrix[0])
    m = len(matrix)

    num_islands = 0

    for i in range(n):
        for j in range(m):
            if not matrix[j][i]:
                continue

            num_islands += 1
            q = [(i, j)]
            matrix[j][i] = 0

            while q:
                x, y = q.pop(0)
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy

                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                        continue

                    if matrix[new_y][new_x] != 1:
                        continue

                    q.append((new_x, new_y))
                    matrix[new_y][new_x] = 0
    return num_islands


input = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
]
input = [[1], [1]]
output = count_islands(input)
print(output)
