# naive - O(2^n) space and time
def find_fibonacci(n):
    if n in [0, 1]:
        return n
    else:
        return find_fibonacci(n - 1) + find_fibonacci(n - 2)


# bottom-up / DP - O(n) time O(1) space
def find_fibonacci(n):
    prv = 0
    nxt = 1

    for _ in range(n - 1):
        tmp = prv + nxt
        prv = nxt
        nxt = tmp

    return nxt


# recursive top-down solution w/ general additive sequence method - O(n) time and space
def find_fibonacci(n):
    return general_additive_sequence(n, 0, 1)


def general_additive_sequence(n, b1, b2):
    if n == 0:
        return b1
    else:
        return general_additive_sequence(n - 1, b2, b1 + b2)


# top-down / memoization
def find_fibonacci(n):
    dp_table = {}
    return fib_helper(n, dp_table)


def fib_helper(n, dp_table):
    if n in [0, 1]:
        return n
    else:
        if n not in dp_table:
            dp_table[n] = fib_helper(n - 1, dp_table) + fib_helper(n - 2, dp_table)

        return dp_table[n]
