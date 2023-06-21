def find_combinations(n, k):
    current_combo = []
    all_combos = []
    helper(n, k, 1, current_combo, all_combos)
    return all_combos


def helper(n, k, curr_num, current_combo, all_combos):
    if k == len(current_combo):
        all_combos.append(current_combo.copy())
        # print("found 1 combo", all_combos, current_combo)
        return

    if curr_num == n + 1:
        # print("here")
        return

    # print("before", current_combo, all_combos)

    current_combo.append(curr_num)
    # print("after", current_combo, all_combos)
    helper(n, k, curr_num + 1, current_combo, all_combos)
    current_combo.pop()
    helper(n, k, curr_num + 1, current_combo, all_combos)


def count_n_choose_k(n, k):
    if k in [0, n]:
        return 1
    else:
        return count_n_choose_k(n - 1, k - 1) + count_n_choose_k(n - 1, k)


# memoized version
def count_n_choose_k(n, k):
    dp = {}
    return count_n_choose_k_helper(n, k, dp)


def count_n_choose_k_helper(n, k, dp):
    if k in [0, n]:
        return 1
    else:
        if (n, k) not in dp:
            chosen = count_n_choose_k_helper(n - 1, k - 1, dp)
            not_chosen = count_n_choose_k_helper(n - 1, k, dp)
            dp[(n, k)] = chosen + not_chosen

        return dp[(n, k)]
