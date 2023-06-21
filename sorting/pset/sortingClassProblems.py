from heapq import heappop, heappush
import random


def two_sum_sorted(numbers, target):
    hi = len(numbers) - 1
    lo = 0

    while lo < hi:
        summed = numbers[lo] + numbers[hi]
        if summed == target:
            return [lo, hi]
        elif summed < target:
            lo += 1
        else:
            hi -= 1

    return [-1, -1]


def two_sum(numbers, target):
    d = {}

    for i in range(len(numbers)):
        if numbers[i] in d:
            return [d[numbers[i]], i]
        else:
            d[target - numbers[i]] = i

    return [-1, -1]


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


"""Brute force approach"""

"""FIX"""


# add smallest element of all lists to srted until lists are empty
def merge_k_lists_brute_force1(lists):
    srted = None
    while lists:
        min_elt = lists[0].value
        min_idx = 0
        for i in range(len(lists)):
            if lists[i] and lists[i].value < min_elt:
                min_elt = lists[i].value
                min_idx = i

        if srted:
            srted.next = LinkedListNode(min_elt)
        else:
            srted = LinkedListNode(min_elt)

        if not lists[min_idx].next:
            del lists[min_idx]
    return srted


# add all elts to an array, sort it, then convert to LL
def merge_k_lists_brute_force2(lists):
    srted = []
    for i in range(len(lists)):
        n = lists[i]
        while n:
            srted.append(n.value)
            n = n.next

    srted.sort()
    if not srted:
        return

    head = dummy = LinkedListNode(srted[0])

    for i in range(1, len(srted)):
        dummy.next = LinkedListNode(srted[i])
        dummy = dummy.next
    return head


"""Divide and conquer approach"""


def merge_k_lists(lists):
    return merge_k_lists_helper(lists, 0, len(lists) - 1)


def merge_k_lists_helper(lists, start, end):
    if start > end:
        return

    if start == end:
        return lists[start]

    mid = (start + end) // 2

    left = merge_k_lists_helper(lists, start, mid)
    right = merge_k_lists_helper(lists, mid + 1, end)

    return merge(left, right)


def merge(ll1, ll2):
    merged = []

    while ll1 and ll2:
        if ll1.value < ll2.value:
            merged.append(ll1.value)
            ll1 = ll1.next
        else:
            merged.append(ll2.value)
            ll2 = ll2.next

    while ll1:
        merged.append(ll1.value)
        ll1 = ll1.next

    while ll2:
        merged.append(ll2.value)
        ll2 = ll2.next

    if not merged:
        return

    head = dummy = LinkedListNode(merged[0])

    for i in range(1, len(merged)):
        dummy.next = LinkedListNode(merged[i])
        dummy = dummy.next

    return head


"""Min Heap approach"""


def merge_k_lists_heap(lists):
    heap = []

    for i in range(len(lists)):
        while lists[i]:
            heappush(heap, lists[i].value)
            lists[i] = lists[i].next

    if not heap:
        return

    head = dummy = LinkedListNode(heappop(heap))
    while heap:
        dummy.next = LinkedListNode(heappop(heap))
        dummy = dummy.next

    return head


def convert_to_linked_list(arr):
    if not arr:
        return None

    head = dummy = LinkedListNode(arr[0])

    for i in range(1, len(arr)):
        dummy.next = LinkedListNode(arr[i])
        dummy = dummy.next

    return head


def convert_to_arr(ll):
    arr = []
    while ll:
        arr.append(ll.value)
        ll = ll.next
    return arr


a = convert_to_linked_list([1, 3, 5, 7, 9])
b = convert_to_linked_list([0, 2, 4, 6, 8])
# c = convert_to_arr(merge(a, b))

# print(c)

# print(convert_to_arr(merge_k_lists_heap([])))

# a = convert_to_linked_list([1, 2, 3, 4, 5])
# b = convert_to_arr(a)
# print(b)
# while a:
#     print(a.value)
#     a = a.next

# merge_k_lists_brute_force1([])


def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        cur = intervals[i]
        nxt = intervals[i + 1]

        if cur[1] > nxt[0]:
            return 0

    return 1


def find_top_k_frequent_elements(arr, k):
    counts = {}
    for x in arr:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    its = list(counts.items())
    quick_select(its, k)

    return [x[0] for x in its[len(its) - k :]]


def quick_select(arr, k):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        pivot_idx = partition(arr, lo, hi)

        if pivot_idx == len(arr) - k:
            return
        elif pivot_idx < len(arr) - k:
            lo = pivot_idx + 1
        else:
            hi = pivot_idx - 1


def partition(arr, start, end):
    pivot_idx = random.randint(start, end)
    swap(arr, pivot_idx, start)

    l = start
    for r in range(start + 1, end + 1):
        if arr[r][1] < arr[start][1]:
            l += 1
            swap(arr, l, r)

    # swap pivot to the boundary of left and right subarrays
    swap(arr, start, l)

    # return index of where pivot ends up
    return l


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# def find_top_k_frequent_elements(arr, k):
#     """
#     Args:
#      arr(list_int32)
#      k(int32)
#     Returns:
#      list_int32
#     """
#     d = {}

#     for i in range(len(arr)):
#         if arr[i] in d:
#             d[arr[i]] += 1
#         else:
#             d[arr[i]] = 1

#     l = list(d.items())
#     heap = []
#     for i in range(len(l)):
#         heapq.heappush(heap, (-l[i][1], l[i][0]))

#     ans = []
#     for i in range(k):
#         ans.append(heapq.heappop(heap)[1])

#     return ans


ex = [1, 2, 3, 2, 4, 3, 1]
print(find_top_k_frequent_elements(ex, 2))

# ex = [[1, 5], [5, 8], [10, 15]]

# print(can_attend_all_meetings(ex))


def online_median(stream):
    medians = []
    lower = []
    upper = []
    for val in stream:
        median = helper(val, lower, upper)
        medians.append(median)
    return medians


def helper(val, lower, upper):
    # add val to correct heap depending on if its in the upper or lower half of values
    heappush(lower, -val)
    heappush(upper, -lower[0])
    heappop(lower)

    # rebalance heaps so that they are off in size by at most 1
    if len(upper) > len(lower):
        heappush(lower, -upper[0])
        heappop(upper)

    if not lower:
        return upper[0]

    if not upper:
        return -lower[0]

    max_lower = -lower[0]
    min_upper = upper[0]

    # if heaps are perfectly balanced, return the average of the tops of the heaps
    # otherwise, return the top of the larger heap
    if len(lower) == len(upper):
        # change to floating point divisin for exact median
        return (max_lower + min_upper) // 2
    elif len(lower) > len(upper):
        return max_lower
    else:
        return min_upper


# ex = [3, 8, 5, 2]
# print(online_median(ex))
# print(ex, sorted(ex))
