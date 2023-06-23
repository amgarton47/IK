from edge_list_to_adj_list import convert_edge_list_to_adjacency_list


def number_of_connected_components(n, edges):
    adj_list = convert_edge_list_to_adjacency_list(n, edges)
    visited = [0 for _ in range(n)]

    num_components = 0

    for i in range(n):
        if not visited[i]:
            num_components += 1
            dfs(i, visited, adj_list)

    return num_components


# TC: each vertex is pushed and popped from the queue once ~ O(|V|)
# for each vertex, u, we must loop over all of its neighbors i.e degree(u)
# the sum of degree(u) for all u in V = 2*|E|
# final TC: O(|V| + |E|)


# SC: Auxiliary space is O(len(q)) = O(n)
def bfs(s, visited, adj_list):
    q = [s]
    while q:
        v = q.pop(0)
        visited[v] = 1

        for w in adj_list[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1


# same as bfs
def dfs(s, visited, adj_list):
    visited[s] = 1
    for w in adj_list[s]:
        if not visited[w]:
            dfs(w, visited, adj_list)


input = {"n": 6, "edges": [[0, 1], [0, 2], [1, 4], [3, 5]]}

n, edges = input["n"], input["edges"]

output = number_of_connected_components(n, edges)
print(output)
