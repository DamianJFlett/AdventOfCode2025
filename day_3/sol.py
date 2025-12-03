### NO LLM ###

def load_data():
    """
    Load/preprocess data and returns what we need from it
    """
    input = open("input.txt", "r")
    data = []
    for l in input:
        data.append(list(int(x) for x in l[:-1]))
    return data

def p1(data):
    """
    Part 1 
    """
    total = 0
    for row in data:
        maxie = -1
        maxpos = -1
        for index, num in enumerate(row[:-1]):
            if num > maxie:
                maxie = num
                maxpos = index
        num2 = max([int(x) for x in row[maxpos+1:]])
        total += 10*maxie + num2
    print(total)


def p2(data):
    """
    Part 2
    """
    total = 0
    for row in data:
        digits = []
        old_pos = -1
        for i in range(12, 0, -1):
            max_dig = -1
            for index, num in enumerate(row[old_pos + 1:len(row) - (i - 1)]):
                if num > max_dig:
                    max_dig = num
                    start_pos = old_pos+1+index
            digits.append(max_dig)
            old_pos = start_pos
        num = sum(10**i * digits[11-i] for i in range(12))
        print(num)
        total += num
    print(total)
    


def main():
    data = load_data()
    p1(data)
    p2(data)


if __name__ == "__main__":
    main()