memo = {}


# top down, with memo
def minimum_coins(coins, value):
    if value == 0:
        return 0
    if value < 0:
        return float("inf")

    if value not in memo:
        vals = []
        for c in coins:
            vals.append(1 + minimum_coins(coins, value - c))

        memo[value] = min(vals)

    return memo[value]


def minimum_coins(coins, value):
    # construct dp_table
    dp_table = [float("inf") for i in range(value + 1)]
    dp_table[0] = 0

    for i in range(1, value + 1):
        vals = []
        for c in coins:
            if c <= i:
                vals.append(dp_table[i - c])

        dp_table[i] = 1 + min(vals)

    return dp_table[value]


# attempt at constructing solution, not just value of solution
def minimum_coins(coins, value):
    # construct dp_table
    dp_table = [(float("inf"), None) for i in range(value + 1)]
    dp_table[0] = (0, None)

    for i in range(1, value + 1):
        for c in coins:
            if c <= i:
                if dp_table[i - c][0] < dp_table[i][0]:
                    dp_table[i] = (dp_table[i - c][0], i - c)
                else:
                    dp_table[i] = (dp_table[i][0], dp_table[i][1])

        dp_table[i] = (dp_table[i][0] + 1, dp_table[i][1])

    print(get_solution(dp_table, value))
    return dp_table[value][0]


def get_solution(dp_table, value):
    solution = []

    while value > 0:
        print(value)
        prev = dp_table[value][1]
        solution.append(value - prev)
        value -= prev

    print(v)

    return solution


input = {"coins": [1, 3, 5], "value": 9}

# input = {
#     "coins": [
#         83,
#         57,
#         52,
#         64,
#         65,
#         97,
#         53,
#         22,
#         74,
#         54,
#         43,
#         75,
#         8,
#         6,
#         15,
#         58,
#         12,
#         27,
#         68,
#         38,
#         2,
#         14,
#         42,
#         19,
#         26,
#         29,
#         78,
#         85,
#         93,
#         80,
#         87,
#         79,
#         92,
#         51,
#         39,
#         94,
#         34,
#         73,
#         11,
#         81,
#         69,
#         36,
#         99,
#         32,
#         66,
#         88,
#         17,
#         82,
#         55,
#         30,
#         72,
#         18,
#         3,
#         9,
#         20,
#         76,
#         46,
#         13,
#         100,
#         25,
#         59,
#         91,
#         28,
#         84,
#         21,
#         33,
#         45,
#         44,
#         89,
#         40,
#         56,
#         49,
#         95,
#         24,
#         62,
#         48,
#         90,
#         41,
#         50,
#         16,
#         61,
#         1,
#         86,
#         35,
#         77,
#         96,
#         70,
#         4,
#         10,
#         71,
#         47,
#         23,
#         5,
#         7,
#         67,
#         31,
#         37,
#         98,
#         60,
#     ],
#     "value": 9900,
# }

coins = input["coins"]
value = input["value"]


output = minimum_coins(coins, value)

print(output)
