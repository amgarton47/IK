from testing import test


def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list


test(bubble_sort)
