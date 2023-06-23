# a tree is a connected, acyclic graph
# so just check that these properties hold
def is_it_a_tree(node_count, edge_start, edge_end):
    visited = [0 for _ in range(node_count)]
    parent = [0 for _ in range(node_count)]

    # build adjacency graph from edge list
    adj_list = [[] for _ in range(node_count)]
    for i in range(len(edge_start)):
        s = edge_start[i]
        e = edge_end[i]

        # if a vertex points to itself, that is a cycle
        if s == e:
            return False

        adj_list[s].append(e)
        adj_list[e].append(s)

    # check that the number of components is 1
    num_components = 0
    for i in range(node_count):
        if not visited[i]:
            # there is more than 1 component so we can return False early
            if num_components > 0:
                return False
            num_components += 1

            # if we find a cycle in the bfs of any vertex, return false
            if bfs(i, visited, adj_list, parent):
                return False

    return True


# a modified bfs that returns True if a cycle was found, false otherwise
def bfs(s, visited, adj_list, parent):
    q = [s]
    while q:
        v = q.pop(0)
        visited[v] = 1

        for w in adj_list[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
                parent[w] = v
            else:
                # we have visited this neighbor before
                # check if it is our parent
                if w != parent[v]:
                    return True
    return False


inputs = [
    {"node_count": 4, "edge_start": [0, 0, 0], "edge_end": [1, 2, 3]},
    {"node_count": 4, "edge_start": [0, 0], "edge_end": [1, 2]},
    {"node_count": 4, "edge_start": [0, 0, 1, 2], "edge_end": [3, 1, 2, 0]},
    {"node_count": 4, "edge_start": [0, 0, 0, 1], "edge_end": [1, 2, 3, 0]},
]

for i in range(len(inputs)):
    input = inputs[i]
    n, s, e = input["node_count"], input["edge_start"], input["edge_end"]

    output = is_it_a_tree(n, s, e)
    print(output)
