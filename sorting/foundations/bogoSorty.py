import random


def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


t = [0] * 15

for i in range(len(t)):
    t[i] = random.randint(0, 50)

print(bogo_sort(t))
