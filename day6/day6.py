#!/usr/bin/env python


def read(path):
    with open(path) as f:
        timers = list(map(int, f.read().strip().split(",")))
    return timers


def slow(timers, num_steps):
    timers = list(timers)
    step = 0
    n = len(timers)
    while step < num_steps:
        to_extend = []
        for j in range(n):
            if timers[j] == 0:
                to_extend.append(8)
                timers[j] = 6
            else:
                timers[j] -= 1
        timers.extend(to_extend)
        step += 1
        n = len(timers)
    return len(timers)


def fast(timers, num_steps):
    counts = [0] * 9
    for timer in timers:
        counts[timer] += 1
    step = 0
    while step < num_steps:
        next_ = [counts[i + 1] for i in range(8)]
        next_[6] += counts[0]
        next_.append(counts[0])
        counts = next_
        step += 1
    return sum(counts)


def part1(timers):
    return fast(timers, 80)


def part2(timers):
    return fast(timers, 256)


def main():

    timers = read("example.txt")
    assert slow(timers, 10) == fast(timers, 10)
    assert part1(timers) == 5934
    assert part2(timers) == 26984457539

    timers = read("input.txt")
    assert part1(timers) == 376194
    assert part2(timers) == 1693022481538

    print("All tests passed.")


if __name__ == "__main__":
    main()
