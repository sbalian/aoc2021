#!/usr/bin/env python

import heapq
import itertools
import math
from collections import defaultdict


class PriorityQueue:

    # From official Python heapq docs ...

    counter = itertools.count()
    REMOVED = "<removed-task>"

    def __init__(self):
        self.items = []
        self.entry_finder = {}

    def add(self, task, priority=0):
        if task in self.entry_finder:
            self.remove(task)
        count = next(PriorityQueue.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.items, entry)

    def remove(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = PriorityQueue.REMOVED

    def pop_task(self):
        while self.items:
            _, _, task = heapq.heappop(self.items)
            if task is not PriorityQueue.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError("pop from an empty priority queue")

    def __len__(self):
        return len(self.entry_finder)


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
    dist = {}
    dist[source] = 0
    q = PriorityQueue()
    q.add(source, dist[source])
    for v in graph:
        if v != source:
            dist[v] = math.inf
            q.add(v, dist[v])

    while len(q) != 0:
        u = q.pop_task()
        if u == target:
            return dist[u]
        for v in graph[u]:
            alt = dist[u] + grid[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt
                q.add(v, alt)

    raise RuntimeError("target not reached")


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
    assert shortest_path_length(grid, expand=True) == 3022
    print("All tests passed.")


if __name__ == "__main__":
    main()
