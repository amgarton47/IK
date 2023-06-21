from testing import test


# def counting_sort(arr):
#     output = [0 for _ in range(len(arr))]
#     counts = [0 for i in range(4 * (10**5))]

#     for n in arr:
#         counts[n] += 1

#     for i in range(1, len(counts)):
#         counts[i] += counts[i - 1]

#     for i in range(len(arr)):
#         output[counts[arr[i]] - 1] = arr[i]
#         counts[arr[i]] -= 1

#     return output


# def counting_sort(arr):
#     counts = {}

#     for i in range(len(arr)):
#         if arr[i] in counts:
#             counts[arr[i]] += 1
#         else:
#             counts[arr[i]] = 1

#     min_elt = min(arr)
#     max_elt = max(arr)

#     idx = 0

#     for i in range(min_elt, max_elt + 1):
#         if i in counts:
#             freq = counts[i]

#             while freq:
#                 arr[idx] = i
#                 idx += 1
#                 freq -= 1
#     return arr


def counting_sort(arr):
    min_elt = min(arr)
    k = max(arr) - min_elt

    counts = [0] * (k + 1)
    for n in arr:
        counts[n - min_elt] += 1

    idx = 0
    elt = min_elt
    for i in range(len(counts)):
        while counts[i]:
            arr[idx] = elt
            idx += 1
            counts[i] -= 1
        elt += 1
    return arr


test(counting_sort)
