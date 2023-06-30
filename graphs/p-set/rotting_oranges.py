from collections import deque


def rotting_oranges(grid):
    num_cols = len(grid[0])
    num_rows = len(grid)

    q = deque()

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 2:
                q.append((i, j))

    time = 0

    while q:
        time += 1
        q_length = len(q)
        for i in range(q_length):
            r, c = q.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_c < 0 or new_r >= num_rows or new_c >= num_cols:
                    continue

                if grid[new_r][new_c] == 1:
                    q.append((new_r, new_c))
                    grid[new_r][new_c] = 2

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                return -1

    return max(0, time - 1)


grid = [[2, 1, 1], [1, 0, 0], [1, 1, 0]]

output = rotting_oranges(grid)
print(output)
