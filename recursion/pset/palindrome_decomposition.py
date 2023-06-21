def generate_palindromic_decompositions(s):
    solutions = []
    helper([], len(s) - 1, solutions)

    breaks = []

    for i in range(len(solutions)):
        new = "" + s[0]
        for j in range(len(solutions[i])):
            if solutions[i][j] == "1":
                new += "|"
            new += s[j + 1]

        breaks.append(new)

    pals = []

    breaks = [i.split("|") for i in breaks]
    pals = []

    for i in range(len(breaks)):
        all_pals = True
        for b in breaks[i]:
            if not is_palindrome(b, 0, len(b) - 1):
                all_pals = False

        if all_pals:
            pals.append(breaks[i])

    pals = ["|".join(pal) for pal in pals]

    return pals


def is_palindrome(s, start, end):
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def helper(slate, n, solutions):
    if n == 0:
        solutions.append("".join(slate))
        return
    else:
        # 0
        slate.append("0")
        helper(slate, n - 1, solutions)
        slate.pop()

        # 1
        slate.append("1")
        helper(slate, n - 1, solutions)
        slate.pop()


ex = "abracadabra"
print(generate_palindromic_decompositions(ex))

# generate all placements of breaks
#   - all binary strings of length n-1 (0 represents no break, 1 does)
# return set of above generated placements where each section is a palindrome
