from math import log


def parse(raw_input):
    raw_banks = raw_input[:-1].split("\n")
    for raw_bank in raw_banks:
        yield list(map(int, raw_bank))


def first_max(nums):
    max_num = nums[0]
    max_ind = 0

    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            max_ind = i

    return max_num, max_ind


def max_bank(bank):
    digit1, start = first_max(bank[:-1])
    digit2 = max(bank[start + 1:])

    return digit1 * 10 + digit2


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    joltage_sum = 0
    for bank in parse(raw_input):
        joltage = max_bank(bank)
        joltage_sum += joltage

    print(joltage_sum)
