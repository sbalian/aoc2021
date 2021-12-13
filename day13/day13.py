#!/usr/bin/env python


def read_data(path):
    with open(path) as f:
        lines = f.read().strip().splitlines()
    i = lines.index("")
    points = lines[:i]
    instructions = lines[i + 1 :]  # noqa
    points = [tuple(map(int, point.split(","))) for point in points]
    instructions = [
        instruction.lstrip("fold along ").split("=")
        for instruction in instructions
    ]
    instructions = [
        (direction, int(value)) for direction, value in instructions
    ]
    return points, instructions


def fold(points, instruction):
    direction, value = instruction
    n = len(points)
    for i in range(n):
        x, y = points[i]
        if direction == "y":
            if y > value:
                diff = y - value
                points[i] = (x, y - 2 * diff)
        else:
            if x > value:
                diff = x - value
                points[i] = (x - 2 * diff, y)
    return list(set(points))


def print_points(points):
    max_x = max(points, key=lambda x: x[0])[0] + 1
    max_y = max(points, key=lambda x: x[1])[1] + 1
    to_output = ""
    for i in range(max_y):
        row = ""
        for j in range(max_x):
            if (j, i) in points:
                row += "#"
            else:
                row += " "
        to_output += row.rstrip() + "\n"
    return to_output.rstrip("\n")


def part2(data):
    points, instructions = data
    for instruction in instructions:
        points = fold(points, instruction)
    return print_points(points)


def part1(data):
    points, instructions = data
    return len(fold(points, instructions[0]))


PART2_ANSWER = """\
###  #  # #  # #### ####  ##  #  # ###
#  # # #  #  # #       # #  # #  # #  #
#  # ##   #### ###    #  #    #  # ###
###  # #  #  # #     #   # ## #  # #  #
# #  # #  #  # #    #    #  # #  # #  #
#  # #  # #  # #    ####  ###  ##  ###\
"""


def main():
    data = read_data("input.txt")
    assert part1(data) == 802
    assert part2(data) == PART2_ANSWER  # should print RKHFZGUB
    print("All tests passed.")


if __name__ == "__main__":
    main()
