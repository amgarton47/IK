from testing import test


def selection_sort(list):
    for i in range(0, len(list)):
        ind = i
        for j in range(i + 1, len(list)):
            if list[j] < list[ind]:
                ind = j
        # swap
        temp = list[ind]
        list[ind] = list[i]
        list[i] = temp

    return list


test(selection_sort)
