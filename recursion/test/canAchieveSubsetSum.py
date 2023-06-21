from subset_tests import tests


# with backtracking (from class)
def check_if_sum_possible(arr, k):
    return helper([], 0, arr, k, 0, False)


def helper(slate, idx, arr, k, curr, non_empty):
    if k == curr and non_empty:
        return True
    elif idx == len(arr):
        return False
    else:
        # e
        if helper(slate, idx + 1, arr, k, curr, non_empty):
            return True

        # i
        slate.append(arr[idx])
        if helper(slate, idx + 1, arr, k, curr + arr[idx], True):
            return True

        slate.pop()

        return False


# bad, not backtracking here when we clearly could
def check_if_sum_possible(arr, k):
    ret = []
    helper([], 0, arr, k, ret)

    for i in range(len(ret)):
        if sum(ret[i]) == k and ret[i] != []:
            return True

    return False


def helper(slate, idx, arr, k, ret):
    if idx == len(arr):
        ret.append(slate)
        return
    else:
        end = idx
        while end < len(arr) and arr[idx] == arr[end]:
            end += 1

        # e
        helper(slate, end, arr, k, ret)

        # i
        for i in range(1, end - idx + 1):
            helper(slate + [arr[idx]] * i, end, arr, k - i * arr[idx], ret)


for t in tests:
    arr, k = t["input"]
    ans = t["output"]
    try:
        assert check_if_sum_possible(arr, k) == ans
    except:
        print(
            "test failed:", arr, k, ans, "your output:", check_if_sum_possible(arr, k)
        )
