def two_sum(arr, target):
    # presort:
    #   two_pointer_solution
    #   binary_search_solution

    # balanced binary_tree -> heap?, RB tree

    # brute_force_solution
    return hash_map_solution(arr, target)


# O(n) memory, O(n) time
def hash_map_solution(arr, target):
    dic = {}

    for i in range(len(arr)):
        if (target - arr[i]) in dic:
            return [dic[target - arr[i]], i]
        else:
            dic[arr[i]] = i

    return []


ex = [2, 7, 11, 15]

print(hash_map_solution(ex, 9))


# three sum ?
# a + b + c = target
# search for a + b = target - c ?


""""""
# intersection of two sorted arrays
# return array of intersection
# constraints: no duplicates in input arrays or output array

# - brute force, for each element in l1 check if its in l2. if so add to output arr

# - use hash table to store elements from l1, then for each elt in l2 if its in the hash table include it in output

# - use two pointers starting at index 0 of each array.
# O(min(n,m)) time
# output = []
# while(p1 < n and p2 < m)
#   if l1[p1] > l2[p2]:
#       p2++
#   elif l2[p2] > l1[p1]:
#       p1++
#   else:
#       add l2[p1] to output
#       prev = l2[p1]
#       while p2 < m and l2[p2] == prev:
#           p2 ++
#       while p1 < n and l2[p2] == prev:
#           p1 ++
# return output

# - binary search approach: for each elt in l1, binary search for it in l2. if it's there, add to output
# O(nlog(m)) time

# two pointer VS binary search
# ----------------------------
# if m and n are roughly equal, TP is better because O(min(n,m)) ~ O(n) < O(nlog(m))
# if one of m and n are small, then TP is worse because O(n) > O(log(m))

# Follow up: what if we wanted the intersection of three sorted arrays?

""""""
# Problem: kth largest elt of arr

# - brute force: sort arr and return arr[n-k]

# - use pq: minheap or  maxheap

# - (randomized) quicksort (actually quickselect):
# - O(n) runtime
# - if pivot idx == n - k, we have found the index of kth largest so return it and we're done
# if pivot idx is less, recurse on right side
# if pivot idx is greater, recurse on left side

# Extra quickselect problems
# - leetcode 973, 347

# NOTE on space complexity analysis
# - in general, we can think of memory usage as aux + input
# - aux can be split into output and working tape/memory
# - we can ignore the space required for the output if it is required across all solutions to the problem to provide clarity on algorithmic comparisons
