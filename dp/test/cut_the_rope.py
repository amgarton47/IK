# top down (memo)
def max_product_from_cut_pieces(n):
    memo = {}
    if n == 3:
        return 2
    if n == 2:
        return 1

    def helper(n):
        if n == 0:
            return 1

        best = -1
        if n not in memo:
            for i in range(1, n + 1):
                new = i * helper(n - i)
                best = max(best, new)
            memo[n] = best

        return memo[n]

    return helper(n)


# bottom up (tab)
def max_product_from_cut_pieces(n):
    pass


n = 6
n = 4
n = 3

print(max_product_from_cut_pieces(n))
