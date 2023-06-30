import time
import random


# same as unique paths I, but certain squares can be blocked off
def count_unique_paths(grid):
    m, n = len(grid[0]), len(grid)
    table = [[0 for _ in range(m)] for _ in range(n)]

    # base cases are the top row and leftmost column since no path can start before/above these locations
    # going left to righ in top row, there is only 1 way to get there (going right that many times)
    # unless a blockade has appeared in which case, there are 0 ways to get to a given cell from thereon
    # same with top to bottom of 1st row

    table[0][0] = 1 if grid[0][0] == 0 else 0
    for col in range(1, m):
        table[0][col] = table[0][col - 1] if grid[0][col] == 0 else 0

    for row in range(1, n):
        table[row][0] = table[row - 1][0] if grid[row][0] == 0 else 0

    # recurrence equation:
    # unique(m,n) =
    #   unique(m-1, n) + unique(m, n-1) IF grid[m][n] != 1
    #   0 if grid[m][n] == 1
    for row in range(1, n):
        for col in range(1, m):
            if grid[row][col] == 1:
                table[row][col] = 0
            else:
                table[row][col] = table[row][col - 1] + table[row - 1][col]

    # cell at bottom right corner of table corresponds to the number of ways to get there in grid
    return table[n - 1][m - 1]


# space optimized by using input as aux DP table (i.e. O(1) space)
def count_unique_paths1(grid):
    m, n = len(grid[0]), len(grid)

    grid[0][0] = 0 if grid[0][0] else 1

    for col in range(1, m):
        grid[0][col] = 0 if grid[0][col] else grid[0][col - 1]

    for row in range(1, n):
        grid[row][0] = 0 if grid[row][0] else grid[row - 1][0]

    for row in range(1, n):
        for col in range(1, m):
            left, above = grid[row][col - 1], grid[row - 1][col]
            grid[row][col] = 0 if grid[row][col] else left + above

    return grid[n - 1][m - 1]


def time_it(function, input):
    start = time.time()
    output = function(input)
    end = time.time()

    return (output, end - start)


def generate_input(m, n):
    grid = [[0 for _ in range(m)] for _ in range(n)]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] = 0 if random.random() >= 0.08 else 1

    return grid


grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# grid = [[0, 1], [0, 0]]

print(count_unique_paths1(grid))

# for i in range(10):
#     m, n = 1000, 1000
#     grid = generate_input(m, n)

#     output, t = time_it(count_unique_paths, grid)
#     print(f"Algorithm 1 output {output} in {t} seconds")

#     output, t = time_it(count_unique_paths1, grid)
#     print(f"Algorithm 2 output {output} in {t} seconds")
