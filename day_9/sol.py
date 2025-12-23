### NO LLM ###

from itertools import combinations
from functools import lru_cache
from shapely import Polygon, plotting
import matplotlib.pyplot as plt

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
    l = abs(p1[0]-p2[0]) + 1
    w = abs(p1[1]-p2[1]) + 1
    return l * w

def p1(data: list[tuple[int, int]]):
    """
    Part 1
    """
    cur = -1
    for index, p1 in enumerate(data):
        for p2 in data[index:]:
            new = bounded_area(p1, p2)
            if  new > cur:
                cur = bounded_area(p1, p2)
    print(cur)


def p2(data: list[tuple[int, int]]):
    """
    Part 2
    """
    g = Polygon(data + [data[0]])
    def valid(p1, p2):
        a1 = (p1[0], p2[1])
        a2 = (p2[0], p1[1])
        a = Polygon((p1, a1, p2, a2, p1))
        return g.contains(a)
    cur = -1
    for index, p1 in enumerate(data):
        for p2 in data[index:]:
            new = bounded_area(p1, p2)
            if  new > cur and valid(p1, p2):
                cur = bounded_area(p1, p2)
    print(cur)

def main():
    data = load_data()
    p1(data)
    p2(data)


if __name__ == "__main__":
    main()