### NO LLM ###

from itertools import combinations
from functools import lru_cache

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


def bounded_area(p1, p2):
    l = abs(p1[0]-p2[0] + 1)
    w = abs(p1[1]-p2[1] + 1)
    return l * w

def p1(data):
    """
    Part 1
    """
    cur = -1
    for p1 in data:
        for p2 in data:
            new = bounded_area(p1, p2)
            if  new > cur:
                cur = bounded_area(p1, p2)
    print(cur)



#IDEA: issue forms if we have another red tile inside?


def bound(data):
    boundary = set()
    for index, red in enumerate(data):
        if index == 0:
            continue
        if data[index - 1][0] == red[0]:
            mi, ma = min(data[index-1][1], red[1]), max(data[index-1][1], red[1])
            for y in range(mi, ma+1):
                boundary.add((red[0], y))
        else:
            mi, ma = min(data[index-1][0], red[0]), max(data[index-1][0], red[0])
            for x in range(mi, ma+1):
                boundary.add((x, red[1]))
    return boundary


#Alright, so if this is too slow(it definitely is) we have to conclude that there's a way to greatly cut down on the size of the set of pairs of reds that are candidates
# Things that might help:
# as is, we consider x1, x2 and x2, x1. Obviously, this is too much but its only double time. Can fix with smth like itertools.combinations.
# Might it be easier to precompute exactly which pairs are elgible?I think this seems most promising, but is it possible? 
# 

def p2(data):
    """
    Part 2
    """
    # @lru_cache(None)
    # def any_in(p1, p2):
    #     a1, a2 = p1
    #     b1, b2 = p2
    #     for index, red in enumerate(data[1:]):
    #         r1, r2 = red
    #         g1, g2 = data[index-1]
    #         if index == 0:
    #             continue
    #         if min(a1, b1) < red[0] < max(a1, b1) and min(a2, b2) < red[1] < max(a2, b2):
    #             return True
    #         if (min(r1, g1) < a1 < max(a1, g1) and min(a2, b2) < red[1] < max(a2, b2)) or (min(r2, g2) < a2 < max(a2, g2) and min(a1, b1) < red[0] < max(a1, b1)):
    #             return True
    #     return False
    i = 0
    boundary = bound(data)
    # things that are invalid can fulfill this! consider the case where wed have like
    """
    #


        #
               .
            #  .
               . 
    """
    @lru_cache(None)
    def any_in(p1, p2):
        a1, a2 = p1
        b1, b2 = p2
        for x1, x2 in boundary:
            if min(a1, b1) < x1 < max(a1, b1) and min(a2, b2) < x2 < max(a2, b2):
                return False
        return True
    combs = combinations(data, r=2)
    possible_combs =  ((x1, x2) for (x1, x2) in combs if any_in(x1, x2))
    cur =   1
    index = 0
    for (p1, p2) in possible_combs:
        index += 1
        new = bounded_area(p1, p2)
        if  new > cur:
            cur = bounded_area(p1, p2)
            x1, x2 = p1, p2
            print(f" updated to {p1}, {p2}, {cur}")

    print(x1, x2)
    print(cur)


def main():
    data = load_data()
    #p1(data)
    p2(data)


if __name__ == "__main__":
    main()