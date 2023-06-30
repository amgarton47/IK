def find_order(words):
    adj_map = {c: set() for word in words for c in word}
    # arrival = {c: -1 for word in words for c in word}
    # departure = {c: -1 for word in words for c in word}

    top_sort = []

    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]

        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                # c1 < c2
                adj_map[c1].add(c2)
                break

    global time
    time = 0

    visited = {}

    def dfs(source):
        global time
        status = visited.get(source)

        if status == 1:
            return True

        if status == -1:
            return False

        visited[source] = -1

        # arrival[source] = time
        # time += 1

        for neighbor in adj_map[source]:
            if not dfs(neighbor):
                return False

            # if arrival[neighbor] == -1:
            #     has_cycle = dfs(neighbor)
            #     if has_cycle:
            #         return True
            # elif departure[neighbor] == -1:
            #     return True

            # departure[neighbor] = time
            # time += 1
        visited[source] = 1
        top_sort.append(source)
        return True

    for key in adj_map.keys():
        if not dfs(key):
            return ""
        # if arrival[key] == -1:
        #     if dfs(key):
        #         return ""

    top_sort.reverse()
    return "".join(top_sort)


words = ["wrt", "wrf", "er", "ett", "rftt"]
# expected: wertf
out = find_order(words)
print(out)
