# recursive - O(n*2^n) time, O(2^n) space
def binary_strings(n):
    if n == 1:
        return ["0", "1"]
    else:
        prev = binary_strings(n - 1)
        new = []
        for s in prev:
            new.append(s + "0")
            new.append(s + "1")
        return new


# iterative - O(n*2^n) time, O(2^n) space
def binary_strings(n):
    strs = ["0", "1"]
    for _ in range(n - 1):
        new = []
        for s in strs:
            new.append(s + "0")
            new.append(s + "1")
        strs = new
    return strs


# memory efficient solution - O(n*2^n) time, O(n) space
def binary_strings(n):
    helper("", n)


def helper(prefix, n):
    if n == 0:
        print(prefix)
    else:
        helper(prefix + "0", n - 1)
        helper(prefix + "1", n - 1)


binary_strings(3)
