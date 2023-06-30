def max_island_size(grid):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    n = len(grid[0])
    m = len(grid)

    largest_island = 0

    for i in range(n):
        for j in range(m):
            if not grid[j][i]:
                continue

            curr_island = 1
            q = [(i, j)]
            grid[j][i] = 0

            while q:
                x, y = q.pop(0)
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy

                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                        continue

                    if grid[new_y][new_x] != 1:
                        continue

                    curr_island += 1

                    q.append((new_x, new_y))
                    grid[new_y][new_x] = 0
            largest_island = max(largest_island, curr_island)
    return largest_island


inputs = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

for i in inputs:
    output = max_island_size(i)
    print(output)
