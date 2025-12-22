### NO LLM ###

from functools import lru_cache

def load_data():
    """
    Load/preprocess data and returns what we need from it
    """
    input = open("input.txt", "r")
    data = {}
    for line in input:
        l = line[:-1].split(" ")
        data[l[0][:-1]] = l[1:]
    return data


def p1(data):
    """
    Part 1
    """
    @lru_cache
    def p1_recurse(cur):
        # returns number of ways to get from you to out
        if "out" in data[cur]:
            return 1
        return sum([p1_recurse(x) for x in data[cur]])
    print(f"Part 1: {p1_recurse("you")}")

def p2(data):
    """
    Part 2
    """
    """
    Part 1
    """
    @lru_cache(None) # lol
    def p2_recurse(cur, seen):
        if "out" in data[cur]:
            if seen == (1, 1):
                return 1
            else:
                return 0
        if cur == "dac":
            seen = (1, seen[1])
        elif cur == "fft":
            seen = (seen[0], 1)
        return sum([p2_recurse(x,seen ) for x in data[cur]])
    print(f"Part 1: {p2_recurse('svr', (0, 0))}")


def main():
    data = load_data()
    p1(data)
    p2(data)


if __name__ == "__main__":
    main()