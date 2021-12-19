#!/usr/bin/env python


def read_hex(path):
    with open(path) as f:
        return f.read().strip()


def hex2bin(hex_):
    bin_ = ""
    for h in hex_:
        bin_ += bin(int(h, 16))[2:].zfill(4)
    return bin_


def array2string(array):
    return "".join(array)


def bin2int(bin_):
    return int(bin_, 2)


def get_version(array, start):
    end = start + 3
    return bin2int(array2string(array[start:end])), end


def get_packet_type_id(array, start):
    return get_version(array, start)


def get_literal(array, start):
    group_starts = []
    for i in range(start, len(array) + start, 5):
        group_starts.append(i)
        if array[i] == "0":
            break
    value = []
    for i in group_starts:
        from_, to = i + 1, i + 5
        value.append(array2string(array[from_:to]))
    return bin2int(array2string(value)), to


def get_length_type_id(array, start):
    return array[start], start + 1


def get_length(array, start):
    to = start + 15
    return bin2int(array2string(array[start:to])), to


def get_num_subpackets(array, start):
    to = start + 11
    return bin2int(array2string(array[start:to])), to


def test_literal():
    array = list(hex2bin("D2FE28"))
    start = 0
    version, start = get_version(array, start)
    packet_type_id, start = get_packet_type_id(array, start)
    assert packet_type_id == 4
    assert version == 6
    assert get_literal(array, start) == (2021, 21)


def test_operator1():
    array = list(hex2bin("38006F45291200"))
    start = 0
    version, start = get_version(array, start)
    packet_type_id, start = get_packet_type_id(array, start)
    assert version == 1
    assert packet_type_id == 6
    length_type_id, start = get_length_type_id(array, start)
    assert length_type_id == "0"
    length, start = get_length(array, start)
    assert length == 27


def test_operator2():
    array = list(hex2bin("EE00D40C823060"))
    start = 0
    version, start = get_version(array, start)
    packet_type_id, start = get_packet_type_id(array, start)
    assert version == 7
    assert packet_type_id == 3
    length_type_id, start = get_length_type_id(array, start)
    assert length_type_id == "1"
    n, start = get_num_subpackets(array, start)
    assert n == 3


class Parser:
    def __init__(self, hex_):
        self.versions = []
        self.array = list(hex2bin(hex_))

    def parse(self, start):
        version, start = get_version(self.array, start)
        self.versions.append(version)
        packet_type_id, start = get_packet_type_id(self.array, start)

        if packet_type_id == 4:
            value, start = get_literal(self.array, start)
        else:
            length_type_id, start = get_length_type_id(self.array, start)
            if length_type_id == "1":
                n, start = get_num_subpackets(self.array, start)
                i = 0
                while i < n:
                    start = self.parse(start)
                    i += 1
            else:
                length, start = get_length(self.array, start)
                distance = 0
                prev = start
                while distance < length:
                    start = self.parse(start)
                    distance += start - prev
                    prev = start
        return start

    @property
    def sum_versions(self):
        self.parse(0)
        return sum(self.versions)


def test():
    test_literal()
    test_operator1()
    test_operator2()


def part1(hex_):
    return hex2bin(hex_)


def main():
    hex_ = read_hex("input.txt")
    assert Parser(hex_).sum_versions == 984
    print("All tests passed.")


if __name__ == "__main__":
    main()
