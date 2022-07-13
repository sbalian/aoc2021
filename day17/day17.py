#!/usr/bin/env python

import re

INPUT = "target area: x=88..125, y=-157..-103"
EXAMPLE = "target area: x=20..30, y=-10..-5"


def get_target_area(input_string):
    return {
        bound: int(value)
        for bound, value in re.match(
            r"target area: x=(?P<x_min>-\d+|\d+)\.\.(?P<x_max>-\d+|\d+), "
            r"y=(?P<y_min>-\d+|\d+)\.\.(?P<y_max>-\d+|\d+)",
            input_string,
        )
        .groupdict()
        .items()
    }


def part1(target_area):
    max_v = abs(target_area["y_min"]) - 1
    return (max_v * (max_v + 1)) // 2


def main():
    example_target_area = get_target_area(EXAMPLE)
    input_target_area = get_target_area(INPUT)
    assert part1(example_target_area) == 45
    assert part1(input_target_area) == 12246
    print("All tests passed.")


if __name__ == "__main__":
    main()
