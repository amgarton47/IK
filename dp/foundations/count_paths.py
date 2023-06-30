# given an m x n grid, how many unique paths exist between start = (0,0) and end = (m-1, n-1)
# when only moving right and down?

# Note that at each step (as we approach the end), one of row/col increases by 1.
# Thus, a total of m-1 + n-1 moves will be made. So we can reduce our original question to
# "of these m + n - 2  steps, how many of them are right moves (or, equivalently, down moves)?"
# this is the same as (m + n - 2) CHOOSE (m-1)

# Here we instead solve the problem with bottom-up dp


def count_paths(m, n):
    dp_table = [[1 for _ in range(m)] for _ in range(n)]

    for row in range(1, n):
        for col in range(1, m):
            dp_table[row][col] = dp_table[row - 1][col] + dp_table[row][col - 1]

    return dp_table[n - 1][m - 1]


out = count_paths(5, 5)
print(out)
