### NO LLM ###
import numpy as np
import math
def load_data():
    """
    Load/preprocess data and returns what we need from it
    """
    input = open("input.txt", "r")

    data : list[list]= []
    for line in input:
        l = line[:-1].split()
        data.append(l)
    data = np.array(data)
    data = np.transpose(data)
    return data


def load_data2():
    input = open("input.txt", "r")
    data = [list(line.rstrip("\n")) for line in input]
    data = np.array(data)
    data = np.transpose(data)
    return data

def p1(data):
    """
    Part 1
    """
    total = 0
    for row in data:
        if row[4] == "*":
            total += int(row[0])*int(row[1])*int(row[2])*int(row[3])
        else:
            total += int(row[1])+int(row[2])+int(row[0])+int(row[3])
    print(total)


def p2(data):
    total = 0
    running = []
    for row in data:
        if np.all(row == ' '):
            continue
        if row[4] != ' ':
            if running: 
                total += math.prod(running)
            running = []
            op = row[4]
        num = int(''.join(row[:-1])) #python int casting doesn't care about leading/trailing whitespace
        if op == "*":
            running.append(num)
        elif op == '+':
            total += num
        else:
            raise ValueError()
    total += math.prod(running)
    
    print(total)



def main():
    data = load_data()
    p1(data)
    data = load_data2()
    p2(data)


if __name__ == "__main__":
    main()