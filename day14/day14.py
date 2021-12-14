#!/usr/bin/env python

from collections import Counter


def read_data(path):
    with open(path) as f:
        lines = f.read().strip().splitlines()
    template = lines[0]
    rules = {}
    for rule in lines[2:]:
        from_, to = rule.split(" -> ")
        rules[from_] = to
    return template, rules


def part1(template, rules, max_steps):
    steps = 0
    current = list(template)
    while steps < max_steps:
        n = len(current)
        updated = []
        for i in range(n - 1):
            a = current[i]
            b = current[i + 1]
            if (a + b) in rules:
                updated.append(a)
                updated.append(rules[a + b])
        updated.append(b)
        current = updated
        steps += 1

    counter = Counter(current)
    return (
        counter[max(counter, key=counter.get)]
        - counter[min(counter, key=counter.get)]
    )


def part2(template, rules, max_steps):
    counts = {}
    template = list(template)
    for i in range(len(template) - 1):
        counts[template[i] + template[i + 1]] = 1

    for rule in rules.keys():
        if rule not in counts:
            counts[rule] = 0

    elements = list(rules.values())
    for rule in rules.keys():
        elements.extend(list(rule))
    elements = list(set(elements))

    element_counts = {element: 0 for element in elements}
    element_counts.update(dict(Counter(template)))

    steps = 0

    while steps < max_steps:
        new_counts = {pair: 0 for pair in rules.keys()}
        for pair, count in counts.items():
            left, middle, right = pair[0], rules[pair], pair[1]
            new_counts[left + middle] += count
            new_counts[middle + right] += count
            element_counts[middle] += count
        counts = new_counts
        steps += 1

    return (
        element_counts[max(element_counts, key=element_counts.get)]
        - element_counts[min(element_counts, key=element_counts.get)]
    )


def main():
    template, rules = read_data("example.txt")
    assert part1(template, rules, 10) == part2(template, rules, 10) == 1588
    assert part2(template, rules, 40) == 2188189693529
    template, rules = read_data("input.txt")
    assert part1(template, rules, 10) == part2(template, rules, 10) == 2435
    assert part2(template, rules, 40) == 2587447599164
    print("All tests passed.")


if __name__ == "__main__":
    main()
