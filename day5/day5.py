#!/usr/bin/env python

import re
from collections import defaultdict


def read_segments(path, include_diagonals=True):
    r = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    with open(path) as f:
        contents = f.read().strip()
    contents = [tuple(map(int, content)) for content in r.findall(contents)]
    segments = []
    for content in contents:
        segment = Segment(*content)
        if include_diagonals or segment.is_horizontal or segment.is_vertical:
            segments.append(segment)
    return segments


class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.a = (x1, y1)
        self.b = (x2, y2)
        if (
            (self.is_horizontal and self.a[0] > self.b[0])
            or (self.is_vertical and self.a[1] > self.b[1])
            or (self.a[0] > self.b[0])
        ):
            self.a, self.b = self.b, self.a

    @property
    def is_horizontal(self):
        return self.a[1] == self.b[1]

    @property
    def is_vertical(self):
        return self.a[0] == self.b[0]

    def draw(self, world):
        if self.is_horizontal:
            for i in range(self.a[0], self.b[0] + 1):
                world[(i, self.a[1])] += 1
        elif self.is_vertical:
            for i in range(self.a[1], self.b[1] + 1):
                world[(self.a[0], i)] += 1
        else:
            if self.a[1] < self.b[1]:
                increment = 1
            else:
                increment = -1
            current = self.a
            final = self.b
            while current != final:
                world[current] += 1
                current = (current[0] + 1, current[1] + increment)
            world[current] += 1
        return world

    # def crosses(self, other):
    #     if self.is_horizontal and other.is_horizontal:
    #         if self.a[1] != other.a[1]:
    #             return False
    #         if self.a[0] < other.a[0]:
    #             if self.b[0] >= other.a[0]:
    #                 return True
    #         else:
    #             if other.b[0] >= self.b[0]:
    #                 return True
    #     elif self.is_vertical and other.is_vertical:
    #         if self.a[0] != other.a[0]:
    #             return False
    #         if self.a[1] < other.a[1]:
    #             if self.b[1] >= other.a[1]:
    #                 return True
    #         else:
    #             if other.b[1] >= self.b[1]:
    #                 return True
    #     else:
    #         ...


def crossings(segments):
    world = defaultdict(int)
    for segment in segments:
        segment.draw(world)
    crossings_ = 0
    for count in list(world.values()):
        if count > 1:
            crossings_ += 1
    return crossings_


def part1(path):
    segments = read_segments(path, include_diagonals=False)
    return crossings(segments)


def part2(path):
    segments = read_segments(path, include_diagonals=True)
    return crossings(segments)


def main():
    assert part1("example.txt") == 5
    assert part1("input.txt") == 6461
    assert part2("example.txt") == 12
    assert part2("input.txt") == 18065
    print("All tests passed.")


if __name__ == "__main__":
    main()
