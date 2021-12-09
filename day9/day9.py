#!/usr/bin/env python

import functools


def read_heights(path):
    with open(path) as f:
        cols = f.read().strip().splitlines()
    rows = []
    for col in cols:
        rows.append(list(map(int, list(col))))
    return rows


def get_limits(heights):
    return len(heights[0]), len(heights)


def get_neighbors(x, y, heights):
    max_x, max_y = get_limits(heights)
    if x == y == 0:
        return [(1, 0), (0, 1)]
    elif x == (max_x - 1) and y == 0:
        return [(x - 1, 0), (x, 1)]
    elif x == 0 and y == (max_y - 1):
        return [(1, y), (0, y - 1)]
    elif x == (max_x - 1) and y == (max_y - 1):
        return [(x, y - 1), (x - 1, y)]
    elif x == 0:
        return [(x, y + 1), (x, y - 1), (x + 1, y)]
    elif y == 0:
        return [(x + 1, y), (x - 1, y), (x, y + 1)]
    elif x == (max_x - 1):
        return [(x - 1, y), (x, y + 1), (x, y - 1)]
    elif y == (max_y - 1):
        return [(x, y - 1), (x + 1, y), (x - 1, y)]
    else:
        return [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]


def sinks(heights):
    max_x, max_y = get_limits(heights)
    points = set([])
    for i in range(max_x):
        for j in range(max_y):
            if all(
                [
                    heights[q][p] > heights[j][i]
                    for p, q in get_neighbors(i, j, heights)
                ]
            ):
                points.add((i, j))
    return points


def part1(heights):
    answer = 0
    for sink in sinks(heights):
        answer += heights[sink[1]][sink[0]] + 1
    return answer


def count(low_x, low_y, heights, basin_points=None):
    if basin_points is None:
        basin_points = set([])
    basin_points.add((low_x, low_y))
    for p, q in get_neighbors(low_x, low_y, heights):
        if (heights[q][p] - heights[low_y][low_x]) > 0 and heights[q][p] != 9:
            basin_points = count(p, q, heights, basin_points=basin_points)
    return basin_points


def part2(heights):
    return functools.reduce(
        lambda x, y: x * y,
        sorted(
            [
                len(count(low_x, low_y, heights))
                for low_x, low_y in sinks(heights)
            ],
            reverse=True,
        )[:3],
    )


def main():
    heights = read_heights("example.txt")
    assert part1(heights) == 15
    assert part2(heights) == 1134
    heights = read_heights("input.txt")
    assert part1(heights) == 522
    assert part2(heights) == 916688
    print("All tests passed.")


if __name__ == "__main__":
    main()
