#!/usr/bin/env python


def read_records(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    records = []
    for line in lines:
        patterns, output = line.split(" | ")
        records.append((patterns.split(" "), output.split(" ")))
    return records


def part1(records):
    outputs = [output for _, output in records]
    answer = 0
    for output in outputs:
        lengths = list(map(len, output))
        for to_count in [2, 4, 3, 7]:
            answer += lengths.count(to_count)
    return answer


EASY_DIGIT_LENGTHS = {1: 2, 4: 4, 7: 3, 8: 7}


def find_easy_digit(easy_digit, patterns):
    for pattern in patterns:
        if len(pattern) == EASY_DIGIT_LENGTHS[easy_digit]:
            return pattern


def solve(record):
    patterns, output = record

    # 1 and 7 first
    one = find_easy_digit(1, patterns)
    seven = find_easy_digit(7, patterns)

    # Strategy is to determine top, top_left, top_right, bottom, bottom_left,
    # bottom_right and middle

    # The top is what is disjoint between 1 and 7
    top = list(set(seven) - set(one))[0]

    # Now look at 4 and 0, 6, 9
    four = find_easy_digit(4, patterns)
    six_segments = [pattern for pattern in patterns if len(pattern) == 6]
    six_segments = [set(segment) for segment in six_segments]
    four_segment = list(set(four) - set(one))
    for six_segment in six_segments:
        if four_segment[0] in six_segment and four_segment[1] in six_segment:
            continue
        if four_segment[0] in six_segment:
            top_left = four_segment[0]
            middle = four_segment[1]
        else:
            top_left = four_segment[1]
            middle = four_segment[0]

    # Now see what remains when we remove one and the segments we already know
    # from eight, and inspect 6 and 9
    eight = find_easy_digit(8, patterns)
    remainder = list(set(eight) - set(one) - set([top, middle, top_left]))
    unknown1, unknown2 = remainder
    six_segments_without_zero = [
        segment for segment in six_segments if middle in segment
    ]
    for six_or_nine in six_segments_without_zero:
        diff = list(set(eight) - six_or_nine)[0]
        if diff == unknown1:
            bottom_left = unknown1
            bottom = unknown2
        elif diff == unknown2:
            bottom_left = unknown2
            bottom = unknown1
        else:
            top_right = diff
    # This gives us everything except for the last one, and the last one is
    # trivial to find
    bottom_right = list(
        set(eight)
        - set([top, middle, top_left, bottom_left, bottom, top_right])
    )[0]

    # Now build a map of position -> digit
    t, tl, tr, b, bl, br, m = (
        top,
        top_left,
        top_right,
        bottom,
        bottom_left,
        bottom_right,
        middle,
    )
    digits = {
        f"{t}{tl}{tr}{b}{bl}{br}{m}": "8",
        f"{top}{tl}{tr}{b}{bl}{br}": "0",
        f"{top}{tl}{tr}{b}{br}{m}": "9",
        f"{top}{tl}{b}{bl}{br}{m}": "6",
        f"{top}{tl}{b}{br}{m}": "5",
        f"{tl}{tr}{br}{m}": "4",
        f"{top}{tr}{b}{br}{m}": "3",
        f"{top}{tr}{b}{bl}{m}": "2",
        f"{tr}{br}": "1",
        f"{top}{tr}{br}": "7",
    }

    # Sort the keys and the patterns in the output
    digits = {"".join(sorted(k)): v for k, v in digits.items()}
    output = ["".join(sorted(x)) for x in output]
    return int("".join([digits[d] for d in output]))


def part2(records):
    return sum(solve(record) for record in records)


def main():
    records = read_records("input.txt")
    assert part1(records) == 525
    assert part2(records) == 1083859

    print("All tests passed.")


if __name__ == "__main__":
    main()
