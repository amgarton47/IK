from binarytree import tree, Node

# Leet Code #784
# given a string S, you can transform every letter in S to be upper or lower case to create a new string.
# print all possible strings you can create from S.

# example: S = "a1b2"
# output: a1b2, A1b2, A1B2, a1B2


def letter_case_transformation(S):
    lct_helper("", S)


def lct_helper(slate, S):
    # for each character, if it is alphabetic, consider if we upper cased it or lower cased it
    if len(S) == 0:
        print(slate)
        return
    elif not S[0].isalpha():
        lct_helper(slate + S[0], S[1:])
    else:
        # lower
        lct_helper(slate + S[0].lower(), S[1:])

        # upper
        lct_helper(slate + S[0].upper(), S[1:])


# version that passes down pointer rather than smaller S for the subproblem
def lct2(S):
    lct2_helper("", 0, S)


def lct2_helper(slate, ptr, S):
    if ptr == len(S):
        print(slate)
        return
    elif not S[ptr].isalpha():
        lct2_helper(slate + S[ptr], ptr + 1, S)
    else:
        lct2_helper(slate + S[ptr].lower(), ptr + 1, S)
        lct2_helper(slate + S[ptr].upper(), ptr + 1, S)


# version that returns list of combinatorial enumerations, rather than printing one per line
def lct2_list(S):
    ret = []
    lct2_list_helper("", 0, S, ret)
    return ret


def lct2_list_helper(slate, ptr, S, ret):
    if ptr == len(S):
        ret.append(slate)
        return
    elif not S[ptr].isalpha():
        lct2_list_helper(slate + S[ptr], ptr + 1, S, ret)
    else:
        lct2_list_helper(slate + S[ptr].lower(), ptr + 1, S, ret)
        lct2_list_helper(slate + S[ptr].upper(), ptr + 1, S, ret)


# time complexity analysis:
# O(n*2^n)
# TC = (#leaf nodes)*(work of leaf nodes) + (#internal nodes)*(work of internal nodes)
#    = 2^n * n + (2^0 + 2^1 + 2^2 + ... 2^(n-1))*(n)
#    = 2^n * n + O(2^n) * n
#    = 2*(2^n * n)
#    = O(n*2^n)
# * note that the time to print a string of length n is O(n) in time, NOT CONSTANT
# * also, string concatonaion is often a O(n) operation because most languages have immutable strings,
#   so an entire new string is created, and each char is copied over


# Space complexity analysis:
# Only one leaf node is on the call stack at any given time, there is O(n) number of internal nodes on the call stack at any given time
# Now, we find the memory allocation of each node, and multiply by the number of nodes on the call stack at any given time

# for this problem, we have O(1) memory allocation for each leaf node. There is O(n) memory allocation for each internal node (concatonation operation).
# So SC = 1*1 + n*n = O(n^2)


"""Optimized version of above solution. Currently, we are creating a whole new copy of the partial solution at each node in the tree. 
This is due to the fact that strings are immutable in most languages. 
We can instead use a string buffer (dynamically resizing string) to bring down concatonations to O(1) ammortized time."""


def optimized_lct(S):
    ret = []
    optimized_lct_helper([], 0, S, ret)
    return ret


def optimized_lct_helper(slate, ptr, S, ret):
    print(slate, ret)
    if ptr == len(S):
        ret.append("".join(slate))
        return
    elif not S[ptr].isalpha():
        slate.append(S[ptr])
        optimized_lct_helper(slate, ptr + 1, S, ret)
        slate.pop()
    else:
        slate.append(S[ptr].lower())
        optimized_lct_helper(slate, ptr + 1, S, ret)
        slate.pop()

        slate.append(S[ptr].upper())
        optimized_lct_helper(slate, ptr + 1, S, ret)
        slate.pop()


"""Complexity analysis of optimized solution."""
# runtime does not change
# memory is reduced to O(n) since each internal node now does a constant (ammortized) concatonation operation: 1*1 + n*1 = O(n)


# root = Node('slate = "", ptr = 0')
# root.left = Node('upper: slate = "A", ptr = 1')
# root.right = Node('lower: slate = "a", ptr = 1')

# root.left.right = Node('slate = "a1", ptr = 2')
# root.right.right = Node('slate = "a1", ptr = 2')

# print(root)

# input: S = "a1b2"

#                __________________________________________slate = "", ptr = 0_____________
#               /                                                                          \
# upper: slate = "A", ptr = 1_____________                                     lower: slate = "a", ptr = 1_____________
#                                         \                                                                            \
#                             slate = "a1", ptr = 2                                                 slate = "a1", ptr = 2
