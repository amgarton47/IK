# Subsets - based on LC 78
# Given an integer array, nums, print all subsets of nums each on its own line


def subsets(nums):
    subsets_helper([], 0, nums)


def subsets_helper(slate, ptr, nums):
    if ptr == len(nums):
        print("".join(slate))
    else:
        # exclude
        subsets_helper(slate, ptr + 1, nums)
        # include
        slate.append(str(nums[ptr]))
        subsets_helper(slate, ptr + 1, nums)
        slate.pop()


def subsets_optimized(nums):
    ret = []
    subsets_optimized_helper([], 0, nums, ret)
    return ret


def subsets_optimized_helper(slate, ptr, nums, ret):
    if ptr == len(nums):
        ret.append("".join(slate))
    else:
        # exclude
        subsets_optimized_helper(slate, ptr + 1, nums, ret)
        # include
        slate.append(str(nums[ptr]))
        subsets_optimized_helper(slate, ptr + 1, nums, ret)
        slate.pop()


"""Complexity Analysis"""
# TC: 2^n leaf nodes, 2^n - 1 internal nodes
# work per leaf = O(n), work per internal node = O(1)
# so TC = n*2^n + 1(2^n-1) = O(n*2^n)

# SC: O(1) space per leaf and ammortized O(1) per internal node. max 1 leaf node and n internal nodes on call stack at one time.
# so, SC = 1*1 + 1 * n = O(n)
