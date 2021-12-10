#!/usr/bin/env python


def read_records(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    records = []
    for line in lines:
        patterns, output = line.split(" | ")
        records.append((patterns.split(" "), output.split(" ")))
    return records


def solve(record):
    patterns, output = record
    patterns, six_patterns, five_patterns = set(patterns), set([]), set([])
    map_ = {}

    # Trivial numbers first as they have unique numbers of lit segments
    for pattern in patterns:
        if len(pattern) == 2:
            map_[1] = pattern
        elif len(pattern) == 4:
            map_[4] = pattern
        elif len(pattern) == 3:
            map_[7] = pattern
        elif len(pattern) == 7:
            map_[8] = pattern
        elif len(pattern) == 6:
            six_patterns.add(pattern)
        else:
            five_patterns.add(pattern)

    # In six-patterns, only 9 will form itself when overlayed with a 4
    for pattern in six_patterns:
        if set(map_[4]).union(set(pattern)) == set(pattern):
            map_[9] = pattern
            break
    six_patterns.remove(map_[9])

    # When overlaying each six-pattern with each five-pattern only 5 and 6
    # (from five-patterns and six-patterns respectively and confusingly) result
    # in not all segments lit
    for five_pattern in five_patterns:
        for six_pattern in six_patterns:
            if len(set(five_pattern).union(set(six_pattern))) != 7:
                map_[5] = five_pattern
                map_[6] = six_pattern
                break
    five_patterns.remove(map_[5])
    six_patterns.remove(map_[6])

    # We only have the 0 in the six-patterns
    map_[0] = six_patterns.pop()

    # Now only the 3 overlayed with 1 gives itself
    for pattern in five_patterns:
        if set(pattern).union(set(map_[1])) == set(pattern):
            map_[3] = pattern
            break
    five_patterns.remove(map_[3])

    # The last one is the 2
    map_[2] = five_patterns.pop()

    map_ = {"".join(sorted(v)): k for k, v in map_.items()}
    output = ["".join(sorted(x)) for x in output]
    return int("".join([str(map_[x]) for x in output]))


def part2(records):
    return sum(solve(record) for record in records)


def main():
    records = read_records("input.txt")
    assert part2(records) == 1083859
    records = read_records("example.txt")
    assert part2(records) == 5353

    print("All tests passed.")


if __name__ == "__main__":
    main()
