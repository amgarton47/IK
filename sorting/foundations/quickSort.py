from testing import test
from random import randint

"""An implementation of random quicksort"""


def quick_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    helper(arr, 0, len(arr) - 1)
    return arr


def helper(arr, start, end):
    if start >= end:
        return

    # select random pivot
    pivot_idx = randint(start, end)

    # both hoare's and lomuto's pivot algorithms are implemented
    new_pivot_idx = hoares_partition(arr, start, end, pivot_idx)
    # new_pivot_idx = lomutos_partition(arr, start, end, pivot_idx)

    helper(arr, start, new_pivot_idx - 1)
    helper(arr, new_pivot_idx + 1, end)


def lomutos_partition(arr, start, end, pivot_idx):
    swap(arr, pivot_idx, start)

    l = start
    for r in range(start + 1, end + 1):
        if arr[r] < arr[start]:
            l += 1
            swap(arr, l, r)

    # swap pivot to the boundary of left and right subarrays
    swap(arr, start, l)

    # return index of where pivot ends up
    return l


def hoares_partition(arr, start, end, pivot_idx):
    swap(arr, pivot_idx, start)

    l = start + 1
    r = end

    while l <= r:
        if arr[l] < arr[start]:
            l += 1
        elif arr[r] > arr[start]:
            r -= 1
        else:
            # l, r are "stuck"
            swap(arr, l, r)
            l += 1
            r -= 1
    # swap pivot to the boundary of left and right subarrays
    swap(arr, start, r)

    # return index of where pivot ends up
    return r


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


test(quick_sort)

# ex = [4, 2, 1, 3, 8, 7, 5, 6]
# lomuto_partition(ex, 0, len(ex) - 1, 0)
# print(ex)

# ex = [4, 2, 1, 3, 8, 7, 5, 6]
# hoare_partition(ex, 0, len(ex) - 1, 0)
# print(ex)

# print(quick_sort(ex))
