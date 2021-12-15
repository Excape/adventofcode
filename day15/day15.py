from collections import defaultdict
import heapq

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def part_1(risks, max_x, max_y):
    result = find_risk_of_shortest_path(risks, max_x, max_y)
    print(f"total risk: {result}")


def part_2(risks, max_x, max_y):
    full_risks, full_max_x, full_max_y = expand_map(risks, max_x, max_y)
    print(len(full_risks.keys()))

    result = find_risk_of_shortest_path(full_risks, full_max_x, full_max_y)
    print(f"total risk: {result}")


def find_risk_of_shortest_path(risks, max_x, max_y):
    path = find_shortest_path(risks, max_x, max_y)
    print(path)
    return calc_total_risk(path, risks)


def parse_input(lines):
    risks = {}
    for y, row in enumerate(lines):
        cols = [int(c) for c in row]
        for x, risk in enumerate(cols):
            risks[(x, y)] = risk

    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1

    return risks, max_x, max_y


def expand_map(risks, max_x, max_y):
    # expand to the right
    for n in range(1, 5):
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                x2, y2 = (x + n * (max_x + 1), y)
                risks[(x2, y2)] = get_adjusted_risk(x, y, n, risks)

    new_max_x = (max_x + 1) * 5 - 1

    # expand down
    for n in range(5):
        for x in range(new_max_x + 1):
            for y in range(max_y + 1):
                x2, y2 = (x, y + n * (max_y + 1))
                risks[(x2, y2)] = get_adjusted_risk(x, y, n, risks)

    new_max_y = (max_y + 1) * 5 - 1

    return risks, new_max_x, new_max_y


def get_adjusted_risk(x, y, offset, risks):
    r = risks[(x, y)] + offset
    return r if r < 10 else r % 9


def find_shortest_path(risks, max_x, max_y):
    source = (0, 0)
    target = (max_x, max_y)
    visited = set()
    parents = {}
    pq = []
    node_risks = defaultdict(lambda: float("inf"))
    node_risks[source] = 0
    heapq.heappush(pq, (0, source))

    while pq:
        _, node = heapq.heappop(pq)
        if node == target:
            return get_path(target, source, parents)

        visited.add(node)
        x, y = node
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor in visited or not in_bounds(*neighbor, max_x, max_y):
                continue
            new_risk = node_risks[node] + risks[neighbor]
            if node_risks[neighbor] > new_risk:
                parents[neighbor] = node
                node_risks[neighbor] = new_risk
                heapq.heappush(pq, (new_risk, neighbor))


def get_path(target, source, parents):
    path = [target]
    node = target
    while node != source:
        p = parents[node]
        path.append(p)
        node = p
    return path


def calc_total_risk(path, risks):
    return sum(risks[v] for v in path[:-1])


def in_bounds(x, y, max_x, max_y):
    return x >= 0 and y >= 0 and x <= max_x and y <= max_y


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    risks, max_x, max_y = parse_input(lines)
    part_1(risks, max_x, max_y)
    part_2(risks, max_x, max_y)
