memo = {}


def find_fibonacci(n):
    if n in [0, 1]:
        return n

    # -------tabulation 1--------
    prev_three = [0, 1, None]

    for i in range(2, n + 1):
        prev_three[i % 3] = prev_three[(i - 1) % 3] + prev_three[(i - 2) % 3]

    return prev_three[n % 3]

    # -------tabulation 2--------
    # prevprev = 0
    # prev = 1

    # for _ in range(2, n + 1):
    #     n = prevprev + prev
    #     prevprev = prev
    #     prev = n

    # return prev

    # -------memoization--------
    # if n not in memo:
    #     memo[n] = find_fibonacci(n - 1) + find_fibonacci(n - 2)

    # return memo[n]


for i in range(10):
    print(f"fib({i}) = {find_fibonacci(i)}")


def jump_ways(n):
    arr = [1, 1, None]

    for i in range(2, n + 1):
        arr[i % 3] = arr[(i - 1) % 3] + arr[(i - 2) % 3]

    return arr[n % 3]


for i in range(1, 11):
    print(f"jumpways({i}) = {jump_ways(i)}")
