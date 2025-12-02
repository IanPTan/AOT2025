from part1 import parse


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()

    curr = 50
    count = 0
    for dir, dis in parse(raw_input):
        delta = dir * dis
        raw_curr = curr + delta

        countd = (abs(raw_curr) // 100\
               + (curr != 0 and raw_curr < 0)\
               + (raw_curr == 0))\
               * (delta != 0)

        count += countd
        curr = raw_curr % 100

        #print(dir, "\t", dis, "\t", curr, "\t", raw_curr, "\t", countd)
    
    print(count)
