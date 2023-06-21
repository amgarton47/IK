def find_combinations(n, k):
    ret = []
    helper(n, 1, k, [], ret)
    return ret


def helper(n, i, k, slate, ret):
    if k == len(slate):
        ret.append(slate[:])
    elif i == n + 1:
        return
    else:
        # i
        slate.append(i)
        helper(n, i + 1, k, slate, ret)
        slate.pop()
        # e
        helper(n, i + 1, k, slate, ret)


ex = find_combinations(5, 2)
print(ex)
