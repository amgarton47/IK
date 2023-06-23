def check_if_eulerian_cycle_exists(n, edges):
    # eulerian cycle exists <=> degree of each vertex is even

    v_degrees = [0 for _ in range(n)]

    for e in edges:
        v_degrees[e[0]] += 1
        v_degrees[e[1]] += 1

    for key in v_degrees:
        if v_degrees[key] % 2 == 1:
            return False
    return True


input = {
    "n": 5,
    "edges": [[0, 1], [0, 2], [1, 3], [3, 0], [3, 2], [4, 3], [4, 0]],
}  # true
input = {  # false
    "n": 6,
    "edges": [
        [0, 4],
        [0, 5],
        [1, 2],
        [2, 3],
        [3, 1],
        [4, 3],
    ],
}

new_input = [input["n"], input["edges"]]
n, edges = new_input

output = check_if_eulerian_cycle_exists(n, edges)

print(output)
