def parse_input(lines):
    coords = []
    folds = []
    for line in lines:
        if line.startswith("fold"):
            parts = line.split(" ")
            dim_n = parts[2].split("=")
            folds.append((dim_n[0], int(dim_n[1])))
        elif line:
            x_y = line.split(",")
            coords.append((int(x_y[0]), int(x_y[1])))

    return coords, folds


def fill_grid(grid, coords):
    for x, y in coords:
        grid[y][x] = "#"


def fold_grid(grid, fold, bbox):
    dim, n = fold
    max_x, max_y = bbox
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if in_bounds(x, y, max_x, max_y) and needs_fold(x, y, dim, n):
                x2, y2 = get_mirrored_pos(x, y, dim, n)
                if in_bounds(x2, y2, max_x, max_y) and grid[y2][x2] == "#":
                    grid[y][x] = "#"

    if dim == "y":
        return (bbox[0], n - 1)
    return (n - 1, bbox[1])


def in_bounds(x, y, max_x, max_y):
    return x <= max_x and y <= max_y


def needs_fold(x, y, dim, n):
    if dim == "y":
        return y < n
    else:
        return x < n


def get_mirrored_pos(x, y, dim, n):
    if dim == "y":
        y2 = n + (n - y)
        return x, y2
    else:
        x2 = n + (n - x)
        return x2, y


def print_grid(grid, bbox):
    x, y = bbox
    for line in grid[: y + 1]:
        print(*line[: x + 1])
    print()


def count_dots(grid, bbox):
    max_x, max_y = bbox
    return sum(grid[y][: max_x + 1].count("#") for y in range(max_y + 1))


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    coords, folds = parse_input(lines)
    max_x = max(x for x, y in coords)
    max_y = max(y for x, y in coords)
    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    fill_grid(grid, coords)

    bbox = (max_x, max_y)
    for fold in folds:
        print(fold)
        print(bbox)
        bbox = fold_grid(grid, fold, bbox)

    print_grid(grid, bbox)
    dots = count_dots(grid, bbox)
    print(f"there are {dots} visible dots")
