### NO LLM ###
### Run this one on a fast cpu TT

import math
from collections import defaultdict
from itertools import combinations
def load_data():
    """
    Load/preprocess data and returns what we need from it
    """
    input = open("input.txt", "r")
    data = []
    for line in input:
        l = line[:-1]
        data.append(l.split(","))
    data = [[int(x) for x in row] for row in data]
    data = [tuple(x) for x in data]
    return data

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)


def p1(data):
    """
    Part 1
    """
    num_pairs = 10000
    num_mult = 3
    pairs = list(combinations(data, r=2))
    dists = [dist(p1, p2) for (p1, p2) in pairs]
    popped = []
    #take shortest distance pairs
    for i in range(num_pairs):
        #hack to make this operation faster from stackoverflow post https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
        index_min = min(range(len(dists)), key=dists.__getitem__)
        dists.pop(index_min)
        p1, p2 = pairs.pop(index_min)
        popped.append((p1, p2))
    circuits = []
    # build circuits
    for (p1, p2) in popped:
        locs = []
        for x in circuits:
            if p1 in x or p2 in x:
                locs.append(x)
        else:
            circuits.append({p1, p2})
        if locs:
            merged = set.union(*locs, {p1, p2})
            for x in locs:
                circuits.remove(x)
            circuits.append(merged)
        else:
            circuits.append({p1, p2})
    #get soln
    lens = [len(x) for x in circuits]
    lens.sort(reverse = True)
    print(f"Part 1 Solution: {math.prod([x for x in lens[:num_mult]])}")


def p2(data):
    """
    Part 2
    """
    pairs = list(combinations(data, r=2))
    dists = [dist(p1, p2) for (p1, p2) in pairs]
    circuits = []
    while True:
        #hack to make this operation faster from stackoverflow post https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
        index_min = min(range(len(dists)), key=dists.__getitem__)
        dists.pop(index_min)
        p1, p2 = pairs.pop(index_min)
        locs = []
        for x in circuits:
            if p1 in x or p2 in x:
                locs.append(x)
        else:
            circuits.append({p1, p2})
        if locs:
            merged = set.union(*locs, {p1, p2})
            for x in locs:
                circuits.remove(x)
            circuits.append(merged)
        else:
            circuits.append({p1, p2})
        if len(circuits[-1]) == len(data):
            #IDFK why we get a bunch of unmerged length 2 circuits at the beginning but we do. Last element is always the full circuit though
            break
    print(f"Part 1 Solution: {p1[0]*p2[0]}")


def main():
    data = load_data()
    p1(data)
    p2(data)


if __name__ == "__main__":
    main()