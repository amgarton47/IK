def convert_edge_list_to_adjacency_list(n, edges):
    adj_list = [[] for _ in range(n)]

    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[0]].sort()
        adj_list[e[1]].append(e[0])
        adj_list[e[1]].sort()

    return adj_list


import bisect


def convert_edge_list_to_adjacency_list(n, edges):
    adj_list = [[] for _ in range(n)]

    for e in edges:
        bisect.insort(adj_list[e[0]], e[1])
        bisect.insort(adj_list[e[1]], e[0])

    return adj_list


# input = {"n": 5, "edges": [[0, 1], [1, 4], [1, 2], [1, 3], [3, 4]]}

# n, edges = input["n"], input["edges"]

# output = convert_edge_list_to_adjacency_list(n, edges)

# print(output)
