def what(board):
    board = list(reversed(board))
    for i in range(len(board)):
        if i % 2 != 0:
            board[i] = board[i][::-1]

    dx = 6
    board_dim = len(board)
    n = board_dim * board_dim

    adj_list = [[] for _ in range(n)]

    for cell in range(n):
        for die_roll in range(1, dx + 1):
            if cell + die_roll <= n:
                r, c = get_row_and_col(cell + die_roll, board_dim)
                move = board[r][c]
                if move == -1:
                    adj_list[cell].append(cell + die_roll)
                else:
                    adj_list[cell].append(move)

    distance = [-1] * (n + 1)
    path = [-1] * (n + 1)

    def bfs(s):
        distance[s] = 0
        q = [s]
        path[s] = 0

        while q:
            v = q.pop(0)

            if v == n:
                return distance[v]
            for w in adj_list[v]:
                if distance[w] == -1:
                    distance[w] = distance[v] + 1
                    path[w] = v
                    q.append(w)

        return distance[n - 1]

    ans = bfs(0)
    print(distance)
    print("path", path)

    return ans


def get_row_and_col(n, board_dim):
    # if n < 1 or n > board_dim * board_dim:
    #     raise Exception(f"board position '{n}' out of board range")

    row = (n - 1) // board_dim
    col = (n - 1) % board_dim
    return row, col


board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]

# board = [
#     [-1, -1, 19, 10, -1],
#     [2, -1, -1, 6, -1],
#     [-1, 17, -1, 19, -1],
#     [25, -1, 20, -1, -1],
#     [-1, -1, -1, -1, 15],
# ]

board = [
    [-1, 1, 2, -1],
    [2, 13, 15, -1],
    [-1, 10, -1, -1],
    [-1, 6, 2, 8],
]

# 12, 5, 0

# [
#     [-1, 6, 2, 8],
#     [-1, -1, 10, -1],
#     [2, 13, 15, -1],
#     [-1, 2, 1, -1],
# ]

# output = what(board)
# print(output)

for i in range(1, 101):
    print(get_row_and_col(i, 10))
