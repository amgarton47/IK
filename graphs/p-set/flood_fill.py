def flood_fill(pixel_row, pixel_column, new_color, image):
    w = len(image[0])
    h = len(image)

    q = [(pixel_row, pixel_column)]
    old_color = image[pixel_row][pixel_column]
    image[pixel_row][pixel_column] = new_color

    seen = set()
    seen.add((pixel_row, pixel_column))

    while q:
        v = q.pop(0)
        r, c = v

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r = r + dr
            new_c = c + dc

            if new_r < 0 or new_c < 0 or new_r >= h or new_c >= w:
                continue

            if image[new_r][new_c] != old_color:
                continue

            if (new_r, new_c) in seen:
                continue

            image[new_r][new_c] = new_color
            q.append((new_r, new_c))
            seen.add((new_r, new_c))

    return image


input = {
    "pixel_row": 0,
    "pixel_column": 1,
    "new_color": 2,
    "image": [[0, 1, 3], [1, 1, 1], [1, 5, 4]],
}

input = {
    "pixel_row": 0,
    "pixel_column": 4,
    "new_color": 7,
    "image": [[7, 7, 7, 7, 7, 7]],
}


row, col, new_color, image = (
    input["pixel_row"],
    input["pixel_column"],
    input["new_color"],
    input["image"],
)

out = flood_fill(row, col, new_color, image)

print(out)
