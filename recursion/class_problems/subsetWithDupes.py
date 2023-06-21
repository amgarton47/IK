def get_distinct_subsets(s):
    ret = []
    s = list(s)
    s.sort()
    s = "".join(s)
    helper(s, 0, [], ret)
    return list(sorted(ret))


def helper(s, idx, slate, ret):
    if idx == len(s):
        ret.append("".join(slate))
        return
    else:
        end = idx
        while end < len(s) and s[end] == s[idx]:
            end += 1
        # e
        helper(s, end, slate, ret)

        # i
        for _ in range(1, end - idx + 1):
            slate.append(s[idx])
            helper(s, end, slate, ret)

        for _ in range(1, end - idx + 1):
            slate.pop()


ex = "aba"
print(get_distinct_subsets(ex))
