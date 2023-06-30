from collections import deque


def zombie_cluster(zombies):
    visited = [0 for j in range(len(zombies[0]))]

    def bfs(s):
        visited[s] = 1
        q = deque([s])

        while q:
            node = q.popleft()

            for i in range(len(zombies[node])):
                if zombies[node][i] == "1" and not visited[i]:
                    visited[i] = 1
                    q.append(i)

    num_clusters = 0
    for i in range(len(zombies)):
        if not visited[i]:
            bfs(i)
            num_clusters += 1

    return num_clusters


input = [
    "10000",
    "01000",
    "00100",
    "00010",
    "00001",
]

input = [
    "1100",
    "1110",
    "0110",
    "0001",
]


output = zombie_cluster(input)

print(output)
