# Backtracking is when you prune nodes of your recursive call sructure if they do not satisfy a target constraint


# e.g. The LCT problem, but we only want to output strings that have at most X capital letters
# As we solve the problem, we can prune any recursive calls that have already failed our constraint

# this does not (usually) reduce the time complexity by an order of magnitude in worst case scenarios,
# but in average case it still can reduce time to run by a significant (although not order of n significant) amount


def optimized_lct(S, x):
    ret = []
    optimized_lct_helper([], 0, S, ret, x)
    return ret


def optimized_lct_helper(slate, ptr, S, ret, x):
    print(slate, ret)
    if ptr == len(S):
        ret.append("".join(slate))
        return
    elif not S[ptr].isalpha():
        slate.append(S[ptr])
        optimized_lct_helper(slate, ptr + 1, S, ret, x)
        slate.pop()
    else:
        slate.append(S[ptr].lower())
        optimized_lct_helper(slate, ptr + 1, S, ret, x)
        slate.pop()

        if x != 0:
            slate.append(S[ptr].upper())
            optimized_lct_helper(slate, ptr + 1, S, ret, x - 1)
            slate.pop()
