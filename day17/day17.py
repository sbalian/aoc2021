#!/usr/bin/env python

import math
import re

INPUT = "target area: x=88..125, y=-157..-103"
EXAMPLE = "target area: x=20..30, y=-10..-5"


def get_target_area(input_string):
    return {
        bound: int(value)
        for bound, value in re.match(
            r"target area: x=(?P<min_x>-\d+|\d+)\.\.(?P<max_x>-\d+|\d+), "
            r"y=(?P<min_y>-\d+|\d+)\.\.(?P<max_y>-\d+|\d+)",
            input_string,
        )
        .groupdict()
        .items()
    }


def find_maximum_vertical_velocity(target_area):
    return abs(target_area["min_y"]) - 1


def part1(target_area):
    max_v = find_maximum_vertical_velocity(target_area)
    return (max_v * (max_v + 1)) // 2


def part2(target_area):
    max_x = target_area["max_x"]
    min_x = target_area["min_x"]
    max_y = target_area["max_y"]
    min_y = target_area["min_y"]

    min_v_x = math.ceil((-1 + math.sqrt(1 + 8 * min_x)) / 2)
    max_v_x = max_x
    min_v_y = min_y
    max_v_y = find_maximum_vertical_velocity(target_area)

    v_allowed = 0

    for v_x in range(min_v_x, max_v_x + 1):
        for v_y in range(min_v_y, max_v_y + 1):
            hit = False
            x, y = 0, 0
            v_x_c = v_x
            v_y_c = v_y
            while (x <= max_x) and (y >= min_y):
                if (min_x <= x <= max_x) and (min_y <= y <= max_y):
                    hit = True
                    v_allowed += 1
                    break
                x += v_x_c
                y += v_y_c
                if v_x_c != 0:
                    v_x_c -= 1
                v_y_c -= 1
            if hit:
                continue
    return v_allowed


def main():
    example_target_area = get_target_area(EXAMPLE)
    input_target_area = get_target_area(INPUT)
    assert part1(example_target_area) == 45
    assert part1(input_target_area) == 12246
    assert part2(example_target_area) == 112
    assert part2(input_target_area) == 3528

    print("All tests passed.")


if __name__ == "__main__":
    main()
