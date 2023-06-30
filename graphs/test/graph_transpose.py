class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


from collections import deque


# naive
def create_transpose(node):
    adj_list = {}

    visited = {}
    visited[node] = 1
    q = deque([node])

    while q:
        v = q.popleft()

        if v not in adj_list:
            adj_list[v.value] = []

        for w in v.neighbors:
            if w not in visited:
                visited[w] = 1
                q.append(w)
            adj_list[v.value].append(w.value)

    new_adj_list = {i + 1: [] for i in range(len(adj_list.keys()))}

    # flip edges
    for node in adj_list:
        for neighbor in adj_list[node]:
            new_adj_list[neighbor].append(node)

    nodes = []
    # build new graph from new_adj_list
    for node in new_adj_list:
        nodes.append(GraphNode(node))

    for node in new_adj_list:
        for neighbor in new_adj_list[node]:
            nodes[node - 1].neighbors.append(nodes[neighbor - 1])

    return nodes[0]


# space efficient
def create_transpose(node):
    old_to_new = {}

    def dfs(s):
        if s in old_to_new:
            return old_to_new[s]
        else:
            old_to_new[s] = GraphNode(s.value)

            for neighbor in s.neighbors:
                new_neighbor = dfs(neighbor)
                new_s = old_to_new[s]
                new_neighbor.neighbors.append(new_s)

            return old_to_new[s]

    return dfs(node)


def print_node(node):
    ret = "val: " + str(node.value) + " children:"

    for n in node.neighbors:
        ret += " " + str(n.value)

    print(ret)


n1 = GraphNode(1)
n2 = GraphNode(2)
n3 = GraphNode(3)
n4 = GraphNode(4)

# n1.neighbors.append(n4)

# n4.neighbors.append(n1)
# n4.neighbors.append(n3)

# n2.neighbors.append(n4)

# n3.neighbors.append(n2)

n1.neighbors.append(n2)
n2.neighbors.append(n3)
n3.neighbors.append(n1)


out = create_transpose(n1)
