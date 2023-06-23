from edge_list_to_adj_list import convert_edge_list_to_adjacency_list


def bfs_traversal(n, edges):
    adj_list = convert_edge_list_to_adjacency_list(n, edges)
    traversal = []
    visited = [0 for _ in range(n)]

    def helper(s, adj_list):
        q = [s]
        visited[s] = 1

        while q:
            v = q.pop(0)
            traversal.append(v)
            for w in adj_list[v]:
                if visited[w] == 0:
                    q.append(w)
                    visited[w] = 1

    for i in range(n):
        if not visited[i]:
            helper(i, adj_list)

    return traversal


input = {"n": 6, "edges": [[0, 1], [0, 2], [0, 4], [2, 3]]}

n, edges = input["n"], input["edges"]

output = bfs_traversal(n, edges)
print(output)
