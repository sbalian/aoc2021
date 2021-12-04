#!/usr/bin/env python


def read_report(path):
    with open(path) as f:
        report = f.read().strip().split("\n")
    return report


def part1(report):
    num_cols, num_rows = len(report[0]), len(report)
    gamma_rate, epsilon_rate = "", ""
    for i in range(num_cols):
        num_zeros, num_ones = 0, 0
        for j in range(num_rows):
            if report[j][i] == "0":
                num_zeros += 1
            else:
                num_ones += 1
        if num_ones > num_zeros:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def _part2(report, rating):
    if rating not in ["oxygen", "co2"]:
        raise ValueError("rating must be oxygen or co2")
    num_cols = len(report[0])
    for i in range(num_cols):
        if len(report) == 1:
            break
        num_zeros, num_ones = 0, 0
        for row in report:
            if row[i] == "1":
                num_ones += 1
            else:
                num_zeros += 1
        if num_ones >= num_zeros and rating == "oxygen":
            to_keep = "1"
        elif num_ones >= num_zeros and rating == "co2":
            to_keep = "0"
        elif num_ones < num_zeros and rating == "oxygen":
            to_keep = "0"
        else:
            to_keep = "1"
        report = [x for x in report if x[i] == to_keep]
    return int(report[0], 2)


def part2(report):
    return _part2(report, "oxygen") * _part2(report, "co2")


def main():
    report = read_report("input.txt")
    assert part1(report) == 2035764
    assert part2(report) == 2817661
    print("All tests passed.")


if __name__ == "__main__":
    main()
