#!/usr/bin/env python


def read_lines(path):
    with open(path) as f:
        lines = f.read().strip().splitlines()
    return lines


def find_error(line):
    stack = []
    for token in line:
        if token in ["(", "<", "{", "["]:
            stack.append(token)
        elif not stack:
            return token
        else:
            left = stack.pop(-1)
            if left == "(" and token == ")":
                continue
            if left == "{" and token == "}":
                continue
            if left == "[" and token == "]":
                continue
            if left == "<" and token == ">":
                continue
            return token  # either returns str for incorrect right token
            # (part 1), or returns list[str] (the left
            # unmatched tokens) (part 2), since all lines are either
            # corrupt or incomplete
    return stack


def part1(lines):
    score = 0
    for line in lines:
        error = find_error(line)
        if not isinstance(error, list):
            if error == "]":
                score += 57
            elif error == ")":
                score += 3
            elif error == "}":
                score += 1197
            else:  # ">"
                score += 25137
    return score


def part2(lines):
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in lines:
        error = find_error(line)
        if isinstance(error, list):
            score = 0
            for bracket in reversed(error):
                score = score * 5 + points[bracket]
            scores.append(score)
    return sorted(scores)[len(scores) // 2]


def main():
    lines = read_lines("input.txt")
    assert part1(lines) == 240123
    assert part2(lines) == 3260812321
    print("All tests passed.")


if __name__ == "__main__":
    main()
