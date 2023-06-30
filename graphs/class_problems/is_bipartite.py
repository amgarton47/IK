# a graph is bipartite if its nodes can be split into two distinct sets, A,B
# such that each edge contains one end point in A and the other in B

from collections import deque


# method 1
# Note that a graph is bipartite <=> there are no odd length cycles present in a graph
# Thus, we can perform bfs until all nodes have been visited and check for
# cross edges that have both endpoints in the same level of the BFS tree
def is_bipartitie(adj_list):
    n = len(adj_list)

    visited = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    level = [-1 for _ in range(n)]

    def bfs(source):
        q = deque([source])
        visited[source] = 1
        level[source] = 0

        while q:
            v = q.popleft()

            for w in adj_list[v]:
                if visited[w] == -1:
                    visited[w] = 1
                    parent[w] = v
                    level[w] = level[v] + 1
                    q.append(w)
                elif parent[v] != w and level[v] == level[w]:
                    return False
        return True

    for i in range(n):
        if visited[i] == -1:
            if not bfs(i):
                return False

    return True


# method 2: colors
def is_bipartite(adj_list):
    n = len(adj_list)
    color = [-1 for _ in range(n)]
    color_map = {0: 1, 1: 0}

    def dfs(s, s_color):
        color[s] = s_color

        for w in adj_list[s]:
            if color[w] == -1:
                if not dfs(w, color_map[s_color]):
                    return False
            elif color[s] == color[w]:
                return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False

    return True


input = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

output = is_bipartitie(input)

print(output)
