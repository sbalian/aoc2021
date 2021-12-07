#!/usr/bin/env python


def read_positions(path):
    with open(path) as f:
        return list(map(int, f.read().strip().split(",")))


def min_cost(positions, part=1):
    fuels = []
    n = len(positions)
    for i in range(max(positions)):
        fuel = []
        for j in range(n):
            diff = abs(i - positions[j])
            if part == 2:
                diff = (diff / 2) * (diff + 1)
            fuel.append(diff)
        fuels.append(sum(fuel))
    return min(fuels)


def main():
    positions = read_positions("input.txt")
    assert min_cost(positions, 1) == 328187
    assert min_cost(positions, 2) == 91257582
    print("All tests passed.")


if __name__ == "__main__":
    main()
