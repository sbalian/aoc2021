#!/usr/bin/env python


def read_instructions(path):
    with open(path) as f:
        return f.read().strip().split("\n")


def part1(instructions):
    horizontal, depth = 0, 0
    for instruction in instructions:
        direction, amount = instruction.split()
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
        elif direction == "up":
            depth -= amount
        else:
            depth += amount
    return horizontal * depth


def part2(instructions):
    aim, horizontal, depth = 0, 0, 0
    for instruction in instructions:
        direction, amount = instruction.split()
        amount = int(amount)
        if direction == "forward":
            horizontal += amount
            depth += aim * amount
        elif direction == "up":
            aim -= amount
        else:
            aim += amount
    return horizontal * depth


def main():
    instructions = read_instructions("input.txt")
    assert part1(instructions) == 1635930
    assert part2(instructions) == 1781819478
    print("All tests passed.")


if __name__ == "__main__":
    main()
