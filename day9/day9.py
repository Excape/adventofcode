from functools import reduce

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # left, right, up, down


def split(line):
    return [int(c) for c in line if c.isdigit()]


def part_1(input):
    lowest_points = find_lowest_points(input)
    point_values = list(map(lambda p: input[p[1]][p[0]], lowest_points))
    sum_risk_level = sum(point_values) + len(point_values)
    print(f"Sum of risk levels: {sum_risk_level}")


def find_lowest_points(input):
    visited = []
    lowest_points = []

    for y, row in enumerate(input):
        for x, n in enumerate(row):
            if (x, y) in visited:
                continue
            if all(
                check_neighbors(x, y, dx, dy, n, input, visited)
                for dx, dy in directions
            ):
                lowest_points.append((x, y))
    return lowest_points


def check_neighbors(x, y, dx, dy, n, input, visited):
    x2, y2 = x + dx, y + dy
    if not check_bounds(x2, y2, input):
        return True
    if input[y2][x2] > n:
        visited.append((x2, y2))
        return True
    return False


def check_bounds(x, y, input):
    return x >= 0 and y >= 0 and y < len(input) and x < len(input[y])


def part_2(input):
    basins = find_basins(input)
    basin_sizes = [len(b) for b in basins]
    top_three = sorted(basin_sizes)[-3:]
    result = reduce(lambda acc, n: acc * n, top_three)
    print(f"top three multiplied: {result}")


def find_basins(input):
    lowest_points = find_lowest_points(input)
    basins = []
    for p in lowest_points:
        basin = [p]
        expand_basin(p, basin, input)
        basins.append(basin)
    return basins


def expand_basin(p, basin, input):
    x, y = p
    for dx, dy in directions:
        x2, y2 = x + dx, y + dy
        if not check_bounds(x2, y2, input):
            continue
        if (x2, y2) in basin or input[y2][x2] == 9:
            continue
        if input[y2][x2] > input[y][x]:
            basin.append((x2, y2))
            expand_basin((x2, y2), basin, input)


with open("input.txt") as f:
    lines = f.readlines()
    input = list(map(split, lines))
    part_1(input)
    part_2(input)
