def generate_all_combinations(arr, target):
    ret = []
    helper([], 0, list(sorted(arr)), target, ret)
    return ret


def helper(slate, idx, arr, target, ret):
    if target == 0:
        ret.append(slate[:])
        return
    elif idx == len(arr) or target < 0 or sum(arr[idx:]) < target:
        return
    else:
        end = idx
        while end < len(arr) and arr[idx] == arr[end]:
            end += 1

        # e
        helper(slate, end, arr, target, ret)

        # i
        for i in range(1, end - idx + 1):
            slate.append(arr[idx])
            helper(slate, end, arr, target - i * arr[idx], ret)

        for i in range(1, end - idx + 1):
            slate.pop()


ex = [i for i in range(1, 26)]
t = 300
ans = generate_all_combinations(ex, t)
print(ans)
