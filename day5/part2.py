from part1 import *


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    id_ranges, item_ids = parse(raw_input)

    count = 0
    for id_min, id_max in id_ranges:
        count += id_max - id_min + 1

    print(count)


# too high 360207272663191
