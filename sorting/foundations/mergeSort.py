from testing import test


def merge_sort(arr):
    helper(arr, 0, len(arr) - 1)
    return arr


def helper(arr, start, end):
    if start == end:
        return

    mid = (start + end) // 2
    helper(arr, start, mid)
    helper(arr, mid + 1, end)

    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    aux = [0] * (end - start + 1)
    i, j = start, mid + 1
    idx = 0

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            aux[idx] = arr[i]
            i += 1
        else:
            aux[idx] = arr[j]
            j += 1
        idx += 1

    while i <= mid:
        aux[idx] = arr[i]
        i += 1
        idx += 1

    while j <= end:
        aux[idx] = arr[j]
        j += 1
        idx += 1

    # print(arr)
    for i in range(len(aux)):
        arr[start + i] = aux[i]
    # print(aux, arr)


# t = [8, 4, 5, 7, 3, 1]
# merge_sort(t)
test(merge_sort)
