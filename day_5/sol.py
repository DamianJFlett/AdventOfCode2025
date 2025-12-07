### NO LLM ###

def load_data():
    """
    Load/preprocess data and returns what we need from it
    """
    input = open("input.txt", "r")
    ranges = []
    ids = []
    mode = 0
    for line in input:
        if line == "\n":
            mode = 1
            continue
        if mode:
            ids.append(int(line[:-1]))
        else:
            ranges.append((int(line[:-1].split("-")[0]), int(line[:-1].split("-")[1])))
    return ranges, ids

def p1(ranges, ids):
    """
    Part 1
    """
    counter = 0
    for id in ids:
        for ran in ranges:
            if ran[0] <=id <=  ran[1]:
                counter += 1
                break
    print(counter)


### hint from bradleysigma: "sort your list of ranges by the lower bound" for step 1
def p2(ranges: list[tuple[int, int]], ids: list[int]):
    """
    Part 2
    """
    ranges.sort(key = lambda x:  x[0])
    new = []
    while ranges:
        a1, a2 = ranges.pop(0)
        while ranges and a2 >= ranges[0][0]:
            b1, b2 = ranges.pop(0)
            a2 = max(a2, b2)
        new.append((a1, a2))
    print(sum([p2-p1+1 for p1, p2 in new]))

def main():
    ranges, ids = load_data()
    p1(ranges, ids)
    p2(ranges, ids)


if __name__ == "__main__":
    main()