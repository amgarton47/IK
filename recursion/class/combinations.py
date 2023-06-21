# Combinations - LC #77
# given an input array of integers and a value k <= n, print all combinations
# of k numbers in the array, each on its own line


# here we just call the generate all subsets function, but we implement backtracking so we stop
# adding to a given combo if we have reached the target combo size (i.e., k)
def combinations(nums, k):
    ret = []
    subsets_optimized_helper([], 0, nums, k, ret)
    return ret


def subsets_optimized_helper(slate, ptr, nums, k, ret):
    if len(slate) == k:
        ret.append("".join(slate))
        return
    elif ptr == len(nums):
        return
    else:
        # exclude
        subsets_optimized_helper(slate, ptr + 1, nums, k, ret)
        # include
        slate.append(str(nums[ptr]))
        subsets_optimized_helper(slate, ptr + 1, nums, k, ret)
        slate.pop()


# prioritization for HW exercises
# 1. Implement solutions from class
# 2. Solve permutations problem (LC #46)
# 3. Solve upLevel problems
# 4. Look at supplementary backtracking material
# 5. subset-sum problem - how many subsets of a nums array add up to at most k
# 6. additional problems: Leet code 22, 51, 90, 47, 131, 50


# google drive link from David: https://drive.google.com/drive/folders/1brtdnW5YNf00K4m8KSbsX7r8a4Z6TjQT

# hints for subset and permutation with duplicates in input list
#   - keep track of how many remaining elements we can add (unique / not in current partial solution) as well as how many elements left we need to add
#   - can add = n - ptr, need to add: k - len(partial_solution)
#   - if need to add is ever less than can add, we can prune that node since it will not be possible to fill up this partial solution


# own
# perform TC and SC analysis of perumutations() function
