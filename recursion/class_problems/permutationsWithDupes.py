def get_permutations(arr):
    ret = []
    arr.sort()
    helper(arr, [], ret)
    return ret


def helper(arr, slate, ret):
    if 0 == len(arr):
        ret.append(slate[:])
    else:
        prev = None
        for i in range(len(arr)):
            if prev != arr[i]:
                slate.append(arr[i])
                b = arr.pop(i)
                helper(arr, slate, ret)
                arr.insert(i, b)
                slate.pop()
            prev = arr[i]


ex = [2, 1, 2]
print(get_permutations(ex))


# n! nodes, each does n work


# [1,2,2]

# sp: [2,2], ps: [1]    sp: [1,2], ps: [2] -> sp:[2] ps: [2,1]   and sp[1]  ps: [2,2]


# [2,2,2]

# [2] [2,2]

# [2,2] [2]

# [2,2,2] []


# prune calls to same elt
