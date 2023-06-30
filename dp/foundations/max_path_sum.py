# bottom up, tabulation solution
def maximum_path_sum(grid):
    optimal_path = []
    m = len(grid)
    n = len(grid[0])

    dp_table = [[0 for _ in range(n)] for _ in range(m)]
    dp_table[0][0] = grid[0][0]

    for i in range(1, n):
        dp_table[0][i] = grid[0][i] + dp_table[0][i - 1]

    for i in range(1, m):
        dp_table[i][0] = grid[i][0] + dp_table[i - 1][0]

    for row in range(1, m):
        for col in range(1, n):
            prev_max_path = None
            left, above = dp_table[row][col - 1], dp_table[row - 1][col]
            if left > above:
                optimal_path.append((row, col - 1))
                prev_max_path = left
            else:
                optimal_path.append((row - 1, col))
                prev_max_path = above
            dp_table[row][col] = prev_max_path + grid[row][col]

    return dp_table[m - 1][n - 1], optimal_path


# top down recursive solution with memoization
def maximum_path_sum(grid):
    memo = {(0, 0): grid[0][0]}
    return helper(len(grid) - 1, len(grid[0]) - 1, grid, memo)


def helper(i, j, grid, memo):
    if (i, j) not in memo:
        if i == 0:
            memo[(i, j)] = helper(i, j - 1, grid, memo) + grid[i][j]
        elif j == 0:
            memo[(i, j)] = helper(i - 1, j, grid, memo) + grid[i][j]
        else:
            memo[(i, j)] = grid[i][j] + max(
                helper(i - 1, j, grid, memo), helper(i, j - 1, grid, memo)
            )

    return memo[(i, j)]


grid = [
    [4, 5, 8],
    [3, 6, 4],
    [2, 4, 7],
]

output = maximum_path_sum(grid)
print(output)
