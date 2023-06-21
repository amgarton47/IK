def permutations(arr):
    phelper("", arr)


def phelper(prefix, arr):
    if len(arr) == 0:
        print(prefix)
    else:
        for i in range(len(arr)):
            phelper(prefix + arr[i], arr[:i] + arr[i + 1 :])


def get_permutations(arr):
    result = []
    helper([], arr, result)
    return result


def helper(prefix, arr, result):
    if len(arr) == 0:
        result.append(prefix)
    else:
        for i in range(len(arr)):
            new_pre = prefix.copy()
            new_pre.append(arr[i])
            helper(new_pre, arr[:i] + arr[i + 1 :], result)


print(get_permutations([1, 2, 3]))
