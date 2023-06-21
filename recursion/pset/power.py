import time


# naive recursive (recursive call stack size is exceeded on large inputs)
def calculate_power(a, b):
    return helper(a, b) % 1000000007


def helper(a, b):
    if b == 0:
        return 1
    else:
        return a * helper(a, b - 1)


# naive iterative (doesn't have recursive call stack issue, but is still slow: O(b))
def helper(a, b):
    c = 1

    for i in range(b):
        print(c)
        c *= a
    return c


# faster
def helper(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return helper(a, b // 2) * helper(a, b // 2)
    else:
        return a * helper(a, b - 1)


# fastest
def cp(a, b):
    mod = 1000000007
    return cp_helper(a, b, mod) % mod


def cp_helper(a, b, mod):
    if b == 0:
        return 1
    if b % 2 == 0:
        x = cp_helper(a, b // 2, mod)
        return (x * x) % mod
    else:
        x = cp_helper(a, (b - 1) // 2, mod)
        return (a * x * x) % mod


# can improve on space complexity by doing this iterativeley (removes memory required for recursive call stack)
def calculate_power(a, b):
    mod = 1000000007
    result = 1
    p_of_2 = a % mod

    while b != 0:
        if b % 2 == 1:
            result = result * p_of_2 % mod

        p_of_2 = p_of_2 * p_of_2 % mod
        b = b // 2
    return result


start = time.time()
print(calculate_power(10000, 10000000))
print("time elapsed:", time.time() - start, "seconds")


start = time.time()
print(cp(10000, 10000000))
print("time elapsed:", time.time() - start, "seconds")
