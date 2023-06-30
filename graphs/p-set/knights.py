def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    dist = [[-1 for _ in range(cols)] for _ in range(rows)]

    q = [(start_row, start_col)]
    dist[start_row][start_col] = 0

    while q:
        v = q.pop(0)
        r, c = v

        if r == end_row and c == end_col:
            return dist[r][c]

        for new_r, new_c in get_moves(r, c, rows, cols):
            if dist[new_r][new_c] == -1:
                q.append((new_r, new_c))
                dist[new_r][new_c] = dist[r][c] + 1

    return -1


def get_moves(row, col, n_rows, n_cols):
    moves = []

    spots = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

    for dx, dy in spots:
        new_x = dx + row
        new_y = dy + col

        if new_x < 0 or new_x >= n_rows or new_y < 0 or new_y >= n_cols:
            continue

        moves.append((new_x, new_y))

    return moves


#  x x x x x
#  x x x x x
#  x x x x x
#  x x x x x
#  x x x x x


output = find_minimum_number_of_moves(5, 5, 0, 0, 4, 1)
print(output)
