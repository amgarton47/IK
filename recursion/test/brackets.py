"""Without backtracking"""


def find_all_well_formed_brackets(n):
    ret = []
    arr = ["("] * n + [")"] * n
    helper(arr, [], ret)
    return ret


def helper(arr, slate, ret):
    if 0 == len(arr) and is_well_formed(slate):
        ret.append("".join(slate[:]))
    else:
        prev = None
        for i in range(len(arr)):
            if prev != arr[i]:
                slate.append(arr[i])
                b = arr.pop(i)
                helper(arr, slate, ret)
                arr.insert(i, b)
                slate.pop()
            prev = arr[i]


def is_well_formed(arr):
    s = []
    for i in range(len(arr)):
        if arr[i] == "(":
            s.append(arr[i])
        else:
            if len(s) == 0:
                return False
            else:
                s.pop(-1)

    return len(s) == 0


"""With backtracking"""


def find_all_well_formed_brackets(n):
    ret = []
    arr = ["("] * n + [")"] * n
    helper(arr, [], ret, n)
    return ret


def helper(arr, slate, ret, n):
    if 0 == len(arr):
        ret.append("".join(slate[:]))
    elif not can_be_well_formed(slate, n):
        print("hi", slate)
        return
    else:
        prev = None
        for i in range(len(arr)):
            if prev != arr[i]:
                slate.append(arr[i])
                b = arr.pop(i)
                helper(arr, slate, ret, n)
                arr.insert(i, b)
                slate.pop()
            prev = arr[i]


def can_be_well_formed(arr, n):
    nl = n
    nr = n

    s = []
    for i in range(len(arr)):
        if arr[i] == "(":
            nl -= 1
            s.append(arr[i])
        else:
            if len(s) == 0:
                return False
            else:
                nr -= 1
                s.pop(-1)

    return len(s) == 0 or nl != 0 or nr != 0


"""From class"""


def find_all_well_formed_brackets(n):
    solutions = []
    helper(n, 0, 0, [], solutions)
    return solutions


def helper(n, num_left, num_right, partial, solutions):
    if num_right > num_left or num_left > n:
        return
    elif num_right == num_left == n:
        solutions.append("".join(partial))
        return
    else:
        partial.append("(")
        helper(n, num_left + 1, num_right, partial, solutions)
        partial.pop()

        partial.append(")")
        helper(n, num_left, num_right + 1, partial, solutions)
        partial.pop()


ex = 3
ans = find_all_well_formed_brackets(ex)
print(ans, len(ans))
