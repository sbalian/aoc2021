#!/usr/bin/env python


def read_grid(path):
    with open(path) as f:
        rows = f.read().strip().splitlines()
    return [list(map(int, list(row))) for row in rows]


def print_grid(grid):
    for row in grid:
        print("\t".join(map(str, row)))


def get_neighbors(i, j, m, n):
    points = [
        (i, j + 1),
        (i, j - 1),
        (i + 1, j),
        (i - 1, j),
        (i + 1, j + 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i - 1, j - 1),
    ]
    return [(p, q) for p, q in points if 0 <= p < m and 0 <= q < n]


def explode(grid, i, j, m, n, flashed):
    if flashed is None:
        flashed = set([])
    if grid[i][j] > 9:
        grid[i][j] = 0
        flashed.add((i, j))
        for p, q in get_neighbors(i, j, m, n):
            if (p, q) not in flashed:
                grid[p][q] += 1
                flashed = explode(grid, p, q, m, n, flashed=flashed)
    return flashed


def evolve(grid, m, n):
    flashed = set([])
    for i in range(m):
        for j in range(n):
            if (i, j) not in flashed:
                grid[i][j] += 1
                flashed = explode(grid, i, j, m, n, flashed)
    return len(flashed)


def part1(grid):
    m = len(grid)
    n = len(grid[0])

    total_flashes = 0
    for _ in range(100):
        flashes = evolve(grid, m, n)
        total_flashes += flashes
    return total_flashes


def part2(grid):
    m = len(grid)
    n = len(grid[0])

    steps = 1
    while evolve(grid, m, n) != m * n:
        steps += 1
    return steps


def main():
    assert part1(read_grid("example.txt")) == 1656
    assert part2(read_grid("example.txt")) == 195

    assert part1(read_grid("input.txt")) == 1739
    assert part2(read_grid("input.txt")) == 324

    print("All tests passed.")


if __name__ == "__main__":
    main()
