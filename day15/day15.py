#!/usr/bin/env python

import math
from collections import defaultdict


def read_grid(path):
    with open(path) as f:
        rows = f.read().strip().splitlines()
    return [list(map(int, list(row))) for row in rows]


def get_neighbors(i, j, cols, rows):
    if j == 0 and i == 0:
        return [(0, 1), (1, 0)]
    elif j == (cols - 1) and i == 0:
        return [(1, j), (0, j - 1)]
    elif i == (rows - 1) and j == 0:
        return [(i, 1), (i - 1, 0)]
    elif i == (rows - 1) and j == (cols - 1):
        return [(i, j - 1), (i - 1, j)]
    elif i == 0:
        return [(0, j + 1), (0, j - 1), (1, j)]
    elif i == (rows - 1):
        return [(i, j + 1), (i, j - 1), (i - 1, j)]
    elif j == 0:
        return [(i, 1), (i + 1, 0), (i - 1, 0)]
    elif j == (cols - 1):
        return [(i - 1, j), (i + 1, j), (i, j - 1)]
    else:
        return [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]


def build_graph(grid):
    rows, cols = len(grid), len(grid[0])
    graph = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            for p, q in get_neighbors(i, j, rows, cols):
                graph[(i, j)].append((p, q))
    return graph


def dijkstra(graph, grid, source, target):

    q = set([])
    dist = {}
    for v in graph:
        dist[v] = math.inf
        q.add(v)
    dist[source] = 0

    while len(q) != 0:
        min_dist = math.inf
        min_v = None
        for v in q:
            if dist[v] < min_dist:
                min_dist = dist[v]
                min_v = v
        u = min_v
        q.remove(u)
        if u == target:
            return dist[target]
        for v in graph[u]:
            alt = dist[u] + grid[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt


def add_value(x, value):
    return (x - 1 + value) % 9 + 1


def expand_grid(grid):
    original_rows, original_cols = len(grid), len(grid[0])
    rows = []
    for i in range(original_rows * 5):
        row = [
            add_value(
                grid[i % original_rows][j % original_cols],
                (i // original_rows) + (j // original_cols),
            )
            for j in range(original_cols * 5)
        ]
        rows.append(row)
    return rows


def shortest_path_length(grid, expand=False):
    if expand:
        grid = expand_grid(grid)
    graph = build_graph(grid)
    rows, cols = len(grid), len(grid[0])
    return dijkstra(graph, grid, (0, 0), (rows - 1, cols - 1))


def main():
    grid = read_grid("example.txt")
    assert shortest_path_length(grid) == 40
    assert shortest_path_length(grid, expand=True) == 315

    grid = read_grid("input.txt")
    assert shortest_path_length(grid) == 698
    # This takes 3 hours ... !
    assert shortest_path_length(grid, expand=True) == 3022
    print("All tests passed.")


if __name__ == "__main__":
    main()
