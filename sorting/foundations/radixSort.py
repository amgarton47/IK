from testing import test
import math


def radix_sort(arr):
    return radix_helper(arr, 10)


def radix_helper(arr, base):
    # this is the max number of digits for elts in arr
    # i.e, the number of times we must perform counting sort
    d = math.ceil(math.log(max(arr), base) + 1)

    for i in range(d):
        arr = counting_sort(arr, i, base)

    return arr


def counting_sort(arr, digit, radix):
    ret = [0] * len(arr)
    counts = [0] * radix

    # count the number of instances of each digit (in "digit" place) for values in arr
    for i in range(len(arr)):
        dig = (arr[i] // radix**digit) % radix
        counts[dig] += 1

    # replace each count in counts with the aggregated number of elements before them
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    # in a backwards fashion we place the elements of arr into ret, sorted by the digit in the "digit" place
    for i in range(len(arr) - 1, -1, -1):
        dig = (arr[i] // radix**digit) % radix
        counts[dig] -= 1
        ret[counts[dig]] = arr[i]

    return ret


# assums all A[i] are floats in the range [0,1).
# Time complexity analysis relies on the A[i] being uniformly distributed over the 10 buckets, i.e. [0.0-0.1), [0.1 - 0.2),...
def bucket_sort(A):
    n = len(A)
    B = []
    for _ in range(n):
        B.append([])

    for i in range(n):
        B[math.floor(n * A[i])].append(A[i])

    for i in range(n):
        B[i].sort()

    result = []
    for i in range(n):
        result += B[i]
    return result


print(bucket_sort([0.1, 0.5, 0.23, 0.45]))
test(radix_sort)
