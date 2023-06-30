def levenshtein_distance(word1, word2):
    n = len(word1)
    m = len(word2)

    # 0 = no change
    # 1 = replace
    # 2 = remove
    # 3 = insert

    table = [[(m + n, [i, j, None]) for j in range(n + 1)] for i in range(m + 1)]

    table[0][0] = (0, [0, 0, "empty string"])
    for i in range(1, n + 1):
        table[0][i] = (i, [i, 0, f"remove {word1[-i]}"])

    for i in range(1, m + 1):
        table[i][0] = (i, [0, i, f"remove {word2[-i]}"])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[-j] == word2[-i]:
                table[i][j] = (
                    min(table[i][j][0], table[i - 1][j - 1][0]),
                    [i - 1, j - 1, "no change"],
                )
            else:
                choice = min(
                    table[i - 1][j - 1][0], table[i][j - 1][0], table[i - 1][j][0]
                )
                operation = ""
                x = i
                y = j
                if choice == table[i - 1][j - 1][0]:
                    operation = f"replace {word1[-j]} with {word2[-i]}"
                    x = i - 1
                    y = j - 1
                elif choice == table[i][j - 1][0]:
                    y = j - 1
                    operation = f"remove {word1[-j]}"
                else:
                    x = i - 1
                    operation = f"insert {word2[-i]}"

                table[i][j] = (1 + choice, [x, y, operation])

    return table[m][n][0], table


# input = {"word1": "q", "word2": "qwe"}
# input = {"word1": "cat", "word2": "bat"}
input = {"word1": "sitting", "word2": "kitten"}

w1, w2 = input["word1"], input["word2"]
output = levenshtein_distance(w1, w2)


def construct(table):
    row = len(table) - 1
    col = len(table[0]) - 1

    coords = [(row, col)]
    sol = []

    while row != 0 and col != 0:
        x, y, choice = table[row][col][1]
        sol.append(choice)
        coords.append((x, y))
        row = x
        col = y

    sol.append("done!")

    # coords.reverse()
    # sol.reverse()
    return coords, sol


print(output[0])
# print(construct(output[1]))
