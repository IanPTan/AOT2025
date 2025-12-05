def parse(raw_input):
    lines = raw_input[:-1].split("\n")

    i = 0
    id_ranges = []
    while lines[i] != "":
        id_min, id_max = map(int, lines[i].split("-"))
        add_range(id_ranges, id_min, id_max)
        i += 1

    i += 1
    item_ids = []
    while i < len(lines):
        item_id = int(lines[i])
        item_ids.append(item_id)
        i += 1

    return id_ranges, item_ids


def scan_ranges(id_ranges, id):
    for i, (id_min, id_max) in enumerate(id_ranges):
        if id_min <= id <= id_max:
            return i

    return None


def add_range(id_ranges, lower, upper):
    lower_i = scan_ranges(id_ranges, lower)
    upper_i = scan_ranges(id_ranges, upper)

    if lower_i == None and upper_i == None:
        id_ranges.append([lower, upper])
        return

    if lower_i != None and upper_i != None and lower_i == upper_i:
        return

    if lower_i != None:
        lower = id_ranges.pop(lower_i)[0]

    if upper_i != None:
        if lower_i != None and lower_i < upper_i:
            upper_i -= 1
        upper = id_ranges.pop(upper_i)[1]

    id_ranges.append([lower, upper])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    id_ranges, item_ids = parse(raw_input)

    count = 0
    for item_id in item_ids:
        count += scan_ranges(id_ranges, item_id) != None

    print(count)
