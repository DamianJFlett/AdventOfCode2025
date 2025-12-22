### NO LLM ###


from ast import literal_eval
import itertools
from functools import lru_cache
from z3 import Int, Optimize

def load_data():
    """
    Load/preprocess data and returns what we need from it
    """
    input = open("test_input.txt", "r")
    data = []
    for line in input:
        l = line[:-1]
        data.append(l.split(" "))
    return data

def execute_seq(cur, seq):
    for a in seq:
        for s in a:
            cur[s] = not cur[s]
    return tuple(cur)

def p1(data):
    """
    Part 1
    """
    #DP THOUGHTGS!
    total = 0
    for row in data:
        goal = tuple([0  if x == '.' else 1 for x in row[0][1:-1]])
        buttons =  [literal_eval(x) for x in row[1:-1]] 
        buttons = [(x,) if type(x) == int else x for x in buttons ]
        length = 0
        while True:
            best = [-1]
            sequences = itertools.permutations(buttons, r = length)
            for seq in sequences:
                if execute_seq([0] * len(goal), seq) == goal:
                    best = seq
                    break
            if best != [-1]:
                break
            length += 1
            
        total += length


    print(f"part 1: {total}")


@lru_cache(None)
def apply_button(button, state):
    new = list(state)
    for x in button:
        new[x] += 1
    return tuple(new)

def p2(data):
    """
    Part 2
    """
    total = 0
    for row in data:
        goal = [int(x) for x in row[-1][1:-1].split(",")]
        buttons =  [literal_eval(x) for x in row[1:-1]] 
        buttons = [(x,) if type(x) == int else x for x in buttons ]
        mat = np.mat([[1 if index in button else 0 for button in buttons] for index, _ in enumerate(goal)])
    
    print(f"part 2: {total}")


def main():
    data = load_data()
    #p1(data)
    p2(data)


if __name__ == "__main__":
    main()