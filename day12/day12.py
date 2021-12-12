#!/usr/bin/env python

from collections import defaultdict


def build_graph(path):
    with open(path) as f:
        lines = f.read().strip().splitlines()
    graph = defaultdict(list)
    for line in lines:
        v1, v2 = line.split("-")
        graph[v1].append(v2)
        graph[v2].append(v1)
    return dict(graph)


class Search:
    def __init__(self, graph, use_twice=None):
        self.graph = graph
        self.paths = set([])
        self.use_once = set([x for x in graph.keys() if x.islower()])
        self.use_twice = use_twice
        if self.use_twice is not None:
            self.use_once.remove(use_twice)

    def dfs(self, source, destination, visited=None, path=None):
        if visited is None:
            visited = []
        if path is None:
            path = []

        if path.count(self.use_twice) > 2:
            return

        if source in self.use_once:
            visited.append(source)

        path.append(source)

        if source == destination:
            self.paths.add(tuple(path))
        else:
            for vertex in self.graph[source]:
                if vertex not in visited:
                    self.dfs(vertex, destination, visited, path)

        path.pop()

        if source in visited:
            visited.remove(source)


def part1(graph):
    search = Search(graph)
    search.dfs("start", "end")
    return len(search.paths)


def part2(graph):
    paths = set([])
    for vertex in graph.keys():
        if vertex == "start" or vertex == "end":
            continue
        if vertex.isupper():
            continue
        search = Search(graph, vertex)
        search.dfs("start", "end")
        paths = paths.union(search.paths)
    return len(paths)


def main():

    graph = build_graph("example1.txt")
    assert part1(graph) == 10
    assert part2(graph) == 36

    graph = build_graph("example2.txt")
    assert part1(graph) == 19
    assert part2(graph) == 103

    graph = build_graph("example3.txt")
    assert part1(graph) == 226
    assert part2(graph) == 3509

    graph = build_graph("input.txt")
    assert part1(graph) == 5228
    assert part2(graph) == 131228

    print("All tests passed.")


if __name__ == "__main__":
    main()
