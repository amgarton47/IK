from collections import deque


# this problem is a direct mapping of cycle detection for directed graphs
#
def can_be_completed(n, a, b):
    adj_list = [[] for _ in range(n)]
    for i in range(len(a)):
        s = a[i]
        e = b[i]
        adj_list[s].append(e)

    visited = [0 for _ in range(n)]
    rec_stack = [0 for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            if has_cycle(i, adj_list, rec_stack, visited):
                return False

    return True


# modified dfs to detect cycles
def has_cycle(source, adj_list, rec_stack, visited):
    visited[source] = 1
    rec_stack[source] = 1

    for w in adj_list[source]:
        if not visited[w]:
            if has_cycle(w, adj_list, rec_stack, visited):
                return True
        elif rec_stack[w]:
            return True

    rec_stack[source] = 0
    return False
