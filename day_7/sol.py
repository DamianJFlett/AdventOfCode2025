### NO LLM ###
from collections import defaultdict
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
    
    return data

def p1(data: list[list[str]]):
    """
    Part 1
    """
    start_pos = (0, data[0].find("S")) # positions as (row, column, counting down)
    next ={start_pos}
    splitters = set()
    for row in data[:-1]:
        new = set()
        for pos in next:
            if data[pos[0]][pos[1]] == "^":
                splitters.add((pos[0], pos[1]))
                new.add((pos[0] +1, pos[1]+1))
                new.add((pos[0]+1, pos[1]-1))
            else:
                new.add((pos[0]+1, pos[1]))
        next = new
    print(f"Part 1: {len(splitters)}")




def p2(data):
    """
    Part 2
    """
    start_pos = (0, data[0].find("S")) # positions as (row, column, counting down)
    @lru_cache
    def p2_recurse(pos):
        if pos[0] >= len(data):
            return 1
        elif data[pos[0]][pos[1]] == "^":
            return p2_recurse((pos[0]+1, pos[1]-1)) + p2_recurse((pos[0]+1, pos[1]+1))
        else:
            return p2_recurse((pos[0]+1, pos[1]))


    print(f"Part 2: { p2_recurse(start_pos)}")

def main():
    data = load_data()
    p1(data)
    p2(data)


if __name__ == "__main__":
    main()