def parse(raw_input):
    lines = raw_input[:-1].split("\n")

    i = 0
    id_ranges = []
    while lines[i] != "":
        id_min, id_max = map(int, lines[i].split("-"))
        id_ranges.append([id_min, id_max])
        i += 1
    id_ranges = jank_merge(id_ranges)

    i += 1
    item_ids = []
    while i < len(lines):
        item_id = int(lines[i])
        item_ids.append(item_id)
        i += 1

    return id_ranges, item_ids


def scan_ranges(id_ranges, id, ignore=-1):
    for i, (id_min, id_max) in enumerate(id_ranges):
        if id_min <= id <= id_max and i != ignore:
            return i

    return None


def grow_range(id_ranges, lower, upper):
    i = 0
    while i < len(id_ranges):
        id_min, id_max = id_ranges[i]

        if id_max < lower or id_min > upper:
            i += 1
            continue

        id_ranges.pop(i)

        if id_min < lower:
            lower = id_min

        if id_max > upper:
            upper = id_max

    return lower, upper


def merge_ranges(id_ranges):
    merged_id_ranges = []

    while len(id_ranges) > 0:
        lower, upper = id_ranges.pop(0)
        lower, upper = grow_range(id_ranges, lower, upper)
        merged_id_ranges.append([lower, upper])

    return merged_id_ranges


def jank_merge(id_ranges):
    old_len = -1
    while old_len != len(id_ranges):
        old_len = len(id_ranges)
        id_ranges = merge_ranges(id_ranges)
    return id_ranges


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    id_ranges, item_ids = parse(raw_input)

    count = 0
    for item_id in item_ids:
        count += scan_ranges(id_ranges, item_id) != None

    print(count)
