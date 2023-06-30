def find_pascal_triangle(n):
    binom_coeffs = n_choose_k(n - 1, n - 1)

    for i in range(n):
        binom_coeffs[i] = binom_coeffs[i][: i + 1]

    return binom_coeffs


def n_choose_k(n, k):
    # rec. fn. : C(n,k) = c(n-1, k-1) + c(n-1, k)
    dp = [[1 for _ in range(k + 1)] for _ in range(n + 1)]

    for row in range(2, n + 1):
        for col in range(1, min(row, k + 1)):
            dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]

    return dp


n = 824
n = 12

output = find_pascal_triangle(n)
print(output)


# an optimization idea:
# each row is a mirror of itself
# so can we just calculate the first half of each row as seen below

# [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
#     [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
#     [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1],
# ]

# [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7],
#     [1, 8, 28, 56, 70, 56, 28],
#     [1, 9, 36, 84, 126, 126, 84],
#     [1, 10, 45, 120, 210, 252, 210],
#     [1, 11, 55, 165, 330, 462, 462],
# ]
