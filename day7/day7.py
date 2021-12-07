#!/usr/bin/env python


def read_positions(path):
    with open(path) as f:
        return list(map(int, f.read().strip().split(",")))


def part1(positions):
    fuels = []
    n = len(positions)
    for i in range(max(positions)):
        fuel = []
        for j in range(n):
            fuel.append(abs(i - positions[j]))
        fuels.append(sum(fuel))
    return min(fuels)


def part2(positions):
    fuels = []
    n = len(positions)
    for i in range(max(positions)):
        fuel = []
        for j in range(n):
            diff = abs(i - positions[j])
            fuel.append((diff / 2) * (diff + 1))
        fuels.append(sum(fuel))
    return min(fuels)


def main():
    positions = read_positions("input.txt")
    assert part1(positions) == 328187
    assert part2(positions) == 91257582
    print("All tests passed.")


if __name__ == "__main__":
    main()
