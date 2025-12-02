from math import sqrt
from part1 import parse, get_len


def prime_factorize(num):
    if num <= 1:
        return set()

    #factors = set([1])
    factors = set()
    factor = 2
    while num > 1:
        if num % factor == 0:
            factors.add(factor)

        while num % factor == 0:
            num /= factor

        factor += 1

    return factors


def split_num(num, len):
    factor = 10 ** len
    groups = []
    while num != 0:
        groups.append(num % factor)
        num //= factor

    return groups[::-1]


def check_num(num, group_lens):
    for group_len in group_lens:
        groups = split_num(num, group_len)

        invalid = True
        for i in range(1, len(groups)):
            if groups[i - 1] != groups[i]:
                invalid = False
                break

        if invalid:
            return True

    return False


def get_group_lens(num_len, factors):
    group_lens = []
    for factor in factors:
        group_lens.append(num_len / factor)

    return group_lens


def check_range(id_min, id_max):
    num_len = get_len(id_min) - 1
    magnitude = 10 ** num_len

    invalid_sum = 0
    for num in range(id_min, id_max + 1):
        if num // magnitude:
            magnitude *= 10
            num_len += 1
            group_lens = get_group_lens(num_len, prime_factorize(num_len))

        if check_num(num, group_lens):
            invalid_sum += num

    return invalid_sum


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    invalid_sum = 0
    for id_min, id_max in parse(raw_input):
        invalid_sum += check_range(id_min, id_max)

    print(invalid_sum)
