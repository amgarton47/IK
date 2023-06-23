from edge_list_to_adj_list import convert_edge_list_to_adjacency_list


# iterative
def dfs_traversal(n, edges):
    adj_list = convert_edge_list_to_adjacency_list(n, edges)
    traversal = []
    visited = [0 for _ in range(n)]

    def helper(s, adj_list):
        stack = [s]
        visited[s] = 1

        while stack:
            v = stack.pop()
            traversal.append(v)
            for w in adj_list[v]:
                if visited[w] == 0:
                    stack.append(w)
                    visited[w] = 1

    for i in range(n):
        if not visited[i]:
            helper(i, adj_list)

    return traversal


# recursive
def dfs_traversal(n, edges):
    adj_list = convert_edge_list_to_adjacency_list(n, edges)
    traversal = []
    visited = [0 for _ in range(n)]

    def recursive_helper(s):
        visited[s] = 1
        traversal.append(s)
        for w in adj_list[s]:
            if not visited[w]:
                recursive_helper(w)

    for i in range(n):
        if not visited[i]:
            recursive_helper(i)
    return traversal


input = {"n": 6, "edges": [[0, 1], [0, 2], [1, 4], [3, 5]]}

n, edges = input["n"], input["edges"]

output = dfs_traversal(n, edges)
print(output)
