from testing import test
import heapq


"""Naive implementation. Requires O(n) auxilliary space."""
# def heap_sort(arr):
#     heapq.heapify(arr)
#     return [heapq.heappop(arr) for _ in range(len(arr))]


"""In place implementation"""


def heap_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # build max-heap from arr
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, len(arr), i)

    # construct sorted list from heap one elt at a time
    # by swapping root with right most elt, sinking root,
    # and then decrementing size of heap and repeating
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


# arr - heap representation
# n   - size of arr (window of arr we are considering as part of heap)
# i   - index to "sink"
def heapify(arr, n, i):
    # find largest of current root and its children
    # assume root is largest to start
    largest = i

    l = i * 2 + 1
    r = i * 2 + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # if root is not largest, swap root and largest, and continue to sink ex-root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# ex = [1, 5, 9, 4, 2, 5, 6, 10]
# print(heap_sort(ex))

# ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(heap_sort(ex))

test(heap_sort)
