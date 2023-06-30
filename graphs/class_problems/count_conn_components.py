def number_of_connected_components(n, edges):
    adj_list = [[] for _ in range(n)]
    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])

    visited = [0 for _ in range(n)]

    def dfs(source):
        visited[source] = 1
        for w in adj_list[source]:
            if not visited[w]:
                dfs(w)

    num_components = 0
    for i in range(n):
        if not visited[i]:
            num_components += 1
            dfs(i)
    return num_components


n, edges = 5, [[0, 1], [1, 2], [0, 2], [3, 4]]
output = number_of_connected_components(n, edges)

print(output)
