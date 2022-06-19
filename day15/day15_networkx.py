#!/usr/bin/env python

import networkx as nx


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
    rows, cols = len(grid), len(grid[0])
    graph = nx.DiGraph()
    for i in range(rows):
        for j in range(cols):
            graph.add_node((i, j))

    for node in graph.nodes:
        for neighbor in get_neighbors(node[0], node[1], rows, cols):
            graph.add_edge(
                node, neighbor, weight=grid[neighbor[0]][neighbor[1]]
            )

    return nx.shortest_path_length(
        graph, (0, 0), (rows - 1, cols - 1), weight="weight"
    )


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
