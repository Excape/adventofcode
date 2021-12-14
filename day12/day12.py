from collections import Counter


def part_1(graph):
    paths = find_all_paths_1(graph)
    print(paths)
    print(f"found {len(paths)} paths")


def part_2(graph):
    paths = find_all_paths_2(graph)
    print(paths)
    print(f"found {len(paths)} paths")


def find_all_paths_1(graph):
    paths = []
    visited = []
    find_paths_1("start", graph, visited, [], paths)
    return paths


def find_all_paths_2(graph):
    paths = []
    visited = []
    find_paths_2("start", graph, visited, [], paths)
    return paths


def find_paths_1(vertex, graph, visited, current_path, paths):
    current_path.append(vertex)
    if vertex == "end":
        paths.append(current_path)
    else:
        if vertex.islower():
            visited.append(vertex)
        for v in graph[vertex]:
            if v not in visited:
                find_paths_1(v, graph, visited[:], current_path[:], paths)


def find_paths_2(vertex, graph, visited, current_path, paths):
    current_path.append(vertex)
    if vertex == "end":
        paths.append(current_path)
    else:
        if vertex.islower():
            visited.append(vertex)
        for v in graph[vertex]:
            if v not in visited or visit_small_cage_allowed(v, visited):
                find_paths_2(v, graph, visited[:], current_path[:], paths)


def visit_small_cage_allowed(vertex, visited):
    if vertex == "start":
        return False
    counter = Counter(visited)
    if any(n > 1 for n in counter.values()):
        return False
    return True


def build_adjacency_list(lines):
    adjacency_list = {}
    for line in lines:
        start_end = line.split("-")
        start, end = start_end[0], start_end[1]
        insert_edge(start, end, adjacency_list)
        insert_edge(end, start, adjacency_list)

    return adjacency_list


def insert_edge(start, end, adj):
    if start in adj:
        adj[start].append(end)
    else:
        adj[start] = [end]


with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    graph = build_adjacency_list(lines)
    part_1(graph)
    part_2(graph)
