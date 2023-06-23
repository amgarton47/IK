def convert_edge_list_to_adjacency_matrix(n, edges):
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for e in edges:
        adj_matrix[e[0]][e[1]] = 1
        adj_matrix[e[1]][e[0]] = 1

    return adj_matrix


def convert_edge_list_to_adjacency_matrix(n, edges):
    adj_matrix = [[False for _ in range(n)] for _ in range(n)]
    for e in edges:
        adj_matrix[e[0]][e[1]] = True
        adj_matrix[e[1]][e[0]] = True

    return adj_matrix


input = {"n": 5, "edges": [[0, 1], [1, 4], [1, 2], [1, 3], [3, 4]]}

n, edges = input["n"], input["edges"]

output = convert_edge_list_to_adjacency_matrix(n, edges)

print(output)
