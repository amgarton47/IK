def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    l = 0
    for r in range(1, len(numbers)):
        if numbers[r] % 2 == 0:
            l += 1
            temp = numbers[l]
            numbers[l] = numbers[r]
            numbers[r] = temp

    temp = numbers[0]
    numbers[0] = numbers[l]
    numbers[l] = temp

    return numbers


# ex = [4, 9, 5, 2, 9, 5, 7, 10]
# print(segregate_evens_and_odds(ex))


"""Idea 2: keep three boundary pointers to separate balls arr into [R...G...unkown...B....]"""


def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    l, m, r = 0, 0, len(balls) - 1

    while m <= r:
        if balls[m] == "R":
            balls[l], balls[m] = balls[m], balls[l]
            m += 1
            l += 1


def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # iteration 1
    l = 0
    for r in range(1, len(balls)):
        if balls[r] == "R":
            l += 1
            temp = balls[l]
            balls[l] = balls[r]
            balls[r] = temp

    temp = balls[0]
    balls[0] = balls[l]
    balls[l] = temp

    # iteration 2
    start = l
    for r in range(start + 1, len(balls)):
        if balls[r] == "G":
            l += 1
            temp = balls[l]
            balls[l] = balls[r]
            balls[r] = temp

    if balls[start] < balls[l]:
        temp = balls[start]
        balls[start] = balls[l]
        balls[l] = temp

    return balls


# b = ["G", "B", "G", "G", "R", "B", "R", "G"]
# b = ["R", "G"]
# b = ["B", "G"]
# print(dutch_flag_sort(b))


def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    zero_ptr = len(second) - 1
    f = s = len(first) - 1

    while f >= 0 and s >= 0:
        if first[f] > second[s]:
            second[zero_ptr] = first[f]
            f -= 1
        else:
            second[zero_ptr] = second[s]
            s -= 1
        zero_ptr -= 1

    while f >= 0:
        second[zero_ptr] = first[f]
        f -= 1
        zero_ptr -= 1
    while s >= 0:
        second[zero_ptr] = second[s]
        s -= 1
        zero_ptr -= 1

    return second


# have ptr to furthest right 0
# have ptr to last nonzero elt of both first and second
# while l >= 0 and r >= 0:
#   put maximum of first[l] and second[r] into second[0_ptr]
#   decrement l or r depending on which was max index
# copy over the remainng elts from both lists (only one should be non empty)


def count_triplets(target, numbers):
    """
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
    """
    numbers.sort()
    total = 0

    for i in range(len(numbers)):
        l = i + 1
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] + numbers[i] < target:
                # l + i + k for k < r will all satisfy condition since list is sorted
                total += r - l
                l += 1
            else:
                r -= 1
    return total


# ex = [5, 0, -1, 3, 2]
#  [-1, 0, 2, 3, 5]
# target = 4
# print(count_triplets(4, ex))
