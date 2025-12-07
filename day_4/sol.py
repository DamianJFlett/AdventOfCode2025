### NO LLM ###
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


def setup(data):
    pass

def get_num_rolls(data, r, c, dirs):
    counter = 0
    for dir in dirs:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < len(data) and 0 <= new_c < len(data[new_r]):
            if data[new_r][new_c] == "@":
                counter += 1
    return counter


def p1(data):
    """
    Part 1
    """
    setup(data)
    acc = 0
    dirs = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0}
    for r, row in enumerate(data):
        for c, tile in enumerate(row):
                if tile == "@" and get_num_rolls(data, r, c, dirs) < 4:
                    acc += 1
    print(acc)
            



def get_num_rolls2(data, r, c, dirs):
    counter = 0
    for dir in dirs:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if 0 <= new_r < len(data) and 0 <= new_c < len(data[new_r]):
            if data[new_r][new_c] == 1:
                counter += 1
    return counter

def p2(data):
    """
    Part 2
    """
    setup(data)
    acc = 0
    locs = set()
    dirs = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0}

    new = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    for r in range(len(data[0])):
        for c in range(len(data)):
            if data[r][c] == "@":
                new[r][c] = 1
    data = new
    x = 1
    while x == 1:
        x = 0
        for r, row in enumerate(data):
            for c, tile in enumerate(row):
                    if tile == 1 and get_num_rolls2(data, r, c, dirs) < 4:
                        x = 1
                        acc += 1
                        locs.add((r, c))
        new = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
        for r in range(len(data[0])):
            for c in range(len(data)):
                if (r, c) in locs:
                    new[r][c] = 0
                else:
                    new[r][c] = data[r][c]
        data = new
    print(acc)

def main():
    data = load_data()
    p1(data)
    p2(data)

if __name__ == "__main__":
    main()