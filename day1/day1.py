#!/usr/bin/env python


def read_report(path):
    with open(path) as f:
        report = [int(m) for m in f.read().strip().split("\n")]
    return report


def part1(path):
    report = read_report(path)
    inc = 0
    for i in range(1, len(report)):
        if report[i] > report[i - 1]:
            inc += 1
    return inc


def part2(path):
    report = read_report(path)
    inc = 0
    for i in range(len(report) - 3):
        if report[i + 3] > report[i]:
            inc += 1
    return inc


def i_have_too_much_time_to_kill():
    # modified from tcbegley solution
    print(
        (
            (ds := list(map(int, open("input.txt").readlines())))
            and (
                sum(d1 < d2 for d1, d2 in zip(ds, ds[1:])),
                sum(ds[i] < ds[i + 3] for i in range(len(ds) - 3)),
            )
        )
    )


def main():
    assert part1("input.txt") == 1400
    assert part2("input.txt") == 1429

    print("All tests passed.")


if __name__ == "__main__":
    main()
