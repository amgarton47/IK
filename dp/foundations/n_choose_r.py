import sys


def n_choose_r(n, r):
    if r > n:
        return 0

    use_tab = True

    if not use_tab:
        memo = {}
        return with_memo(n, r, memo)
    else:
        return with_tabulation(n, r)


# bottom-up
def with_tabulation(n, r):
    if r in [0, n]:
        return 1

    dp_table = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    for row in range(n + 1):
        dp_table[row][0] = 1

    for col in range(r + 1):
        dp_table[col][col] = 1

    for row in range(2, n + 1):
        for col in range(1, min(row, r + 1)):
            dp_table[row][col] = dp_table[row - 1][col - 1] + dp_table[row - 1][col]

    print(dp_table)

    return dp_table[n][r]


# top-down
def with_memo(n, r, memo):
    if r == 0:
        return 1
    elif n == 0:
        return 0

    if (n, r) not in memo:
        memo[(n, r)] = with_memo(n - 1, r - 1, memo) + with_memo(n - 1, r, memo)

    return memo[(n, r)]


# prints the first n levels of pascals triangle by calculating C(n, k) for each spot in the triangle
def print_n_levels_of_pascals_triangle(n):
    for j in range(1, n + 1):
        line = []
        for i in range(j):
            line.append(str(n_choose_r(j - 1, i)))
        print("{:^50}".format(" ".join(line)))


# if __name__ == "__main__":
#     n = sys.argv[1]
#     print_n_levels_of_pascals_triangle(int(n))


print(with_tabulation(5, 2))

print_n_levels_of_pascals_triangle(821)
