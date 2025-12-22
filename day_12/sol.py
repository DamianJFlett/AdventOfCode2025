### NO LLM ###

from functools import lru_cache

def load_data():
    """
    Load/preprocess data and returns what we need from it
    """
    input = open("input.txt", "r")
    data = []
    for line in input:
        l = line[:-1]
        data.append(l)
    i = 0
    l = data[0]
    shapes = []
    temp = []
    while "x" not in l:
        l = data[i]
        if ":" in l:
            temp = []
            n = i + 4
            i += 1
            continue
        if n and i < n:
            temp.append(l)
            i += 1
            continue
        l = data[i]
        shapes.append([[1 if (x1, x2) in [(x1, x2) for x1 in range(3) for x2 in range(3) if temp[x1][x2] == "#"] else 0 for x1 in range(3)] for x2 in range(3)])
        i += 1
    regions = []
    i -= 1
    while i < len(data):
        l = data[i]
        dims = tuple([int(x) for x in l.split(":")[0].split("x")])
        regions.append((dims, tuple([int(x) for x in l.split(":")[1][1:].split(" ")])))
        i += 1
    return shapes, regions


def get_transforms(shapes):
    new = []
    for shape in shapes:
        new.append()
        

def p1(shapes, regions):
    """
    Part 1
    """
    total = 0
    # first dp thought looks like keeping track of what I can make with first n shakes.  Probably need some wlog assumption for speed. 1000 element list of regions
    # Ignore the above its actually stupid
    def can_fit(num, shape):
        if (shape[0]//3 ) *  (shape[1] //3) >= num:
            return True
        return False
    for region in regions:
        print(region)
        x = sum(region[1])
        if can_fit(x, region[0]):
            total += 1
    print(f"part 1 solution: {total}")

def p2(shapes, regions):
    """
    Part 2
    """
    pass


def main():
    shapes, regions = load_data()
    p1(shapes, regions)
    p2(shapes, regions)


if __name__ == "__main__":
    main()