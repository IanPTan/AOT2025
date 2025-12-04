import torch as pt
from torch.nn.functional import conv2d


KERNEL = pt.ones(1, 1, 3, 3, dtype=pt.float32)
KERNEL[0, 0, 1, 1] = 0


def parse(raw_input):
    lines = raw_input[:-1].split("\n")
    grid = []
    for line in lines:
        grid.append([
            1 if char == "@" else 0
            for char in line
            ])
    return grid


def get_moveable(grid):
    neighbors = conv2d(grid[None, None, :, :], KERNEL, padding=1, stride=1)[0, 0]
    moveable = (neighbors < 4) * grid

    return moveable


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        raw_input = f.read()
    
    grid = pt.tensor(parse(raw_input), dtype=pt.float32)

    count = 0
    curr_count = 1

    while curr_count > 0:
        moveable = get_moveable(grid)
        grid -= moveable

        curr_count = moveable.sum().item()
        count += curr_count

    print(count)
    
