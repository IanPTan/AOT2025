from part1 import parse


def first_max(nums, start):
    max_num = nums[start]
    max_ind = start

    for i in range(start + 1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            max_ind = i

    return max_num, max_ind


def max_bank(bank, digits=12):
    bank_len = len(bank)

    joltage = 0
    start = 0
    while digits > 0:
        digits -= 1
        digit, start = first_max(bank[:bank_len - digits], start)
        start += 1
        joltage = joltage * 10 + digit

    return joltage


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    joltage_sum = 0
    for bank in parse(raw_input):
        joltage = max_bank(bank, 12)
        joltage_sum += joltage

    print(joltage_sum)
