#!/usr/bin/env python


import copy
import operator


def read_report(path):
    with open(path) as f:
        report = f.read().strip().split("\n")
    return report


def part1(report):
    num_cols = len(report[0])
    num_rows = len(report)
    freq = [{"0": 0, "1": 0} for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            if report[i][j] == "0":
                freq[j]["0"] += 1
            else:
                freq[j]["1"] += 1
    gamma_rate = int(
        "".join([max(f.items(), key=operator.itemgetter(1))[0] for f in freq]),
        2,
    )
    epsilon_rate = int(
        "".join([min(f.items(), key=operator.itemgetter(1))[0] for f in freq]),
        2,
    )
    return gamma_rate * epsilon_rate


def part2(report):
    oxygen = report
    co2 = copy.copy(oxygen)

    num_cols = len(report[0])

    for i in range(num_cols):
        if len(oxygen) == 1:
            break
        num_zeros = 0
        num_ones = 0
        for row in oxygen:
            if row[i] == "1":
                num_ones += 1
            else:
                num_zeros += 1
        if num_ones >= num_zeros:
            to_keep = "1"
        else:
            to_keep = "0"
        oxygen = [x for x in oxygen if x[i] == to_keep]
    oxygen = int(oxygen[0], 2)

    for i in range(num_cols):
        if len(co2) == 1:
            break
        num_zeros = 0
        num_ones = 0
        for row in co2:
            if row[i] == "1":
                num_ones += 1
            else:
                num_zeros += 1
        if num_ones < num_zeros:
            to_keep = "1"
        else:
            to_keep = "0"
        co2 = [x for x in co2 if x[i] == to_keep]
    co2 = int(co2[0], 2)

    return oxygen * co2


def main():
    report = read_report("input.txt")
    assert part1(report) == 2035764
    assert part2(report) == 2817661
    print("All tests passed.")


if __name__ == "__main__":
    main()
