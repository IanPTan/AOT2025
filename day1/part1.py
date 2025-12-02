def parse(raw_input):
    lines = raw_input.split("\n")[:-1]
    for line in lines:
        dir = 1 if line[0] == "R" else -1
        dis = int(line[1:])
        yield dir, dis


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    curr = 50
    count = 0
    for dir, dis in parse(raw_input):
        curr = (curr + dir * dis) % 100

        if curr == 0:
            count += 1
    
    print(count)
