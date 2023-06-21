def get_all_subsets(bag):
    result = []
    subset_helper([], bag, result)
    return result


def subset_helper(prefix, bag, result):
    if len(bag) == 0:
        result.append(prefix)
    else:
        # exclude
        subset_helper(prefix[:], bag[1:], result)
        # include
        subset_helper(prefix + [bag[0]], bag[1:], result)


"""After solving the previous question, Alice has an idea: 
instead of generating the subsets of a set S directly, why 
not generate all binary strings of length n (where |S| = n), and 
when it’s time to print them out at the leaf level, each leaf prints out the 
elements of S corresponding to the 1 bit positions in its assigned binary string solution. 
Would this algorithm work in correctly printing all subsets of S?"""


def alice(S):
    ret = []
    helper("", len(S), S, ret)
    return ret


def helper(prefix, n, S, ret):
    if n == 0:
        subset = []
        for i in range(len(prefix)):
            if prefix[i] == "1":
                subset.append(S[i])
        ret.append(subset)
    else:
        helper(prefix + "0", n - 1, S, ret)
        helper(prefix + "1", n - 1, S, ret)
