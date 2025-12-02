from math import log


def parse(raw_input):
    id_ranges = raw_input[:-1].split(",")
    for id_range in id_ranges:
        id_min, id_max = id_range.split("-")
        yield int(id_min), int(id_max)


def get_len(num):
    return int(log(num, 10)) + 1


def split_num(num, num_len):
    half_len = num_len / 2
    factor = 10 ** half_len

    half1 = int(num / factor)
    half2 = int(num % factor)

    return half1, half2


def dupe_num(num):
    num_len = get_len(num)
    factor = 10 ** num_len
    num += factor * num

    return num


def get_half_bound(id_min, max_mode=0):
    min_len = get_len(id_min)

    if min_len % 2:
        min_half_len = (min_len - 1) / 2
        return 10 ** min_half_len - max_mode

    half1, half2 = split_num(id_min, min_len)

    if max_mode:
        return half1 - (half2 < half1)
    return half1 + (half2 > half1)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    invalid_sum = 0
    for id_min, id_max in parse(raw_input):
        min_half = get_half_bound(id_min, 0)
        max_half = get_half_bound(id_max, 1)

        for i in range(int(min_half), int(max_half) + 1):
            invalid_sum += dupe_num(i)

    print(invalid_sum)
