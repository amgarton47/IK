def check_if_eulerian_path_exists(n, edges):
    # eulerian path exists <=> # of vertices with odd degree is 0 or 2

    v_degrees = [0 for _ in range(n)]

    for e in edges:
        v_degrees[e[0]] += 1
        v_degrees[e[1]] += 1

    num_odd_degree = 0
    for key in v_degrees:
        if v_degrees[key] % 2 == 1:
            num_odd_degree += 1
            if num_odd_degree > 2:
                return False

    return num_odd_degree in [0, 2]


input = {"n": 4, "edges": [[0, 1], [1, 2], [1, 3], [2, 0], [3, 2]]}  # true
input = {"n": 5, "edges": [[0, 3], [1, 2], [1, 3], [3, 2], [4, 1], [4, 2]]}  # false

n, edges = [input["n"], input["edges"]]

output = check_if_eulerian_path_exists(n, edges)

print(output)
