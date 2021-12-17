import re
from itertools import product


def find_succesful_throws(target):
    dxs = list(range(2 * target["end_x"]))
    dys = list(reversed(range(target["end_y"], 2 * abs(target["end_y"]))))
    hits = {}
    for dx, dy in product(dxs, dys):
        result, max_y = simulate_throw(dx, dy, target)
        if result == "hit":
            hits[(dx, dy)] = max_y
    return hits


def simulate_throw(dx, dy, target):
    x = y = 0
    max_y = y
    while True:
        x += dx
        y += dy
        dx -= 1 if dx > 0 else -1 if dx < 0 else 0
        dy -= 1
        if y > max_y:
            max_y = y
        if inside_target(target, x, y):
            return "hit", max_y
        if overshot(target, x, y):
            return "over", max_y
        if missed_right(target, x, y):
            return "right", max_y
        if missed_left(target, x, y):
            return "left", max_y


def inside_target(target, x, y):
    return (
        x >= target["start_x"]
        and x <= target["end_x"]
        and y <= target["start_y"]
        and y >= target["end_y"]
    )


def overshot(target, x, y):
    return x > target["end_x"] and y < target["start_y"]


def missed_right(target, x, y):
    # assuming the target is at x > 0
    return x > target["end_x"]


def missed_left(target, x, y):
    return y < target["end_y"]


with open("input.txt") as f:
    input = f.readline().rstrip()
    x_range, y_range = re.search("^.+x=(.+),\sy=(.+)$", input).groups()
    start_x, end_x = tuple(map(int, x_range.split("..")))
    end_y, start_y = tuple(map(int, y_range.split("..")))
    target = {"start_x": start_x, "end_x": end_x, "start_y": start_y, "end_y": end_y}

    hits = find_succesful_throws(target)
    print(f"there are {len(hits)} succesful throws")

    max_x, max_y = max(hits, key=hits.get)
    print(max_x, max_y, hits[(max_x, max_y)])
