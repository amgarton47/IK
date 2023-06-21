def tower_of_hanoi(n):
    result = []
    helper(n, 1, 3, 2, result)
    return result


def helper(n, src, dst, aux, result):
    if n == 1:
        print(f"Move disk from {src} to {dst}")
        result.append([src, dst])
    else:
        helper(n - 1, src, aux, dst, result)
        print(f"Move disk from {src} to {dst}")
        result.append([src, dst])
        helper(n - 1, aux, dst, src, result)
