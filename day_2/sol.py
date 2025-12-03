### NO LLM ###

def load_data():
    """
    Load/preprocess data and returns what we need from it
    """
    input = open("input.txt", "r")
    data = []
    data2 = []
    for l in input:
        x = l[:-1]
        for range in x.split(","):
            data.append(tuple(range.split("-")))
            data2 += range.split("-")

    return data

def p1(data):
    """
    Part 1
    """
    data2 = []
    for id1, id2 in data:
        data2 += [str(i) for i in range(int(id1), int(id2))]
    invalid_ids = [int(id) for id in data2 if id[:len(id)//2 ] == id[len(id) // 2 :] and (not (len(id) % 2)) and (len(id) >= 2)]
    print(sum(invalid_ids))


def p2(data):
    """
    Part 2
    """
    data2 = []
    for id1, id2 in data:
        data2 += [str(i) for i in range(int(id1), int(id2))]
    invalid_ids = set()
    for id in data2:
        for modulo in range(2, len(id)+ 1):
            if (not len(id) % modulo) and (len(id) >= modulo) and id == (id[:len(id) // modulo] * modulo):
                invalid_ids.add(int(id))
                break
    print(sum(invalid_ids))

def main():
    data = load_data()
    p1(data)
    p2(data)


if __name__ == "__main__":
    main()