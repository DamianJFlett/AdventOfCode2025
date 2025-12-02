### NO LLM ###


def p1():
    f = open("input.txt", "r")
    rotations = []
    for l in f:
        x = l[0]
        y=int(l[1:-1])
        rotations.append((x, y))
    start_pos = 50
    count = 0
    for r in rotations:
        if r[0] == "R":
            start_pos = (start_pos + r[1]) % 100
        else:
            start_pos = (start_pos - r[1]) % 100
        if start_pos == 0:
            count += 1
    print(count)
        
def p2():
    f = open("input.txt", "r")
    rotations = []
    for l in f:
        x = l[0]
        y=int(l[1:-1])
        rotations.append((x, y))
    start_pos = 50
    count = 0
    for r in rotations:
        old_pos = start_pos
        if r[0] == "R":
            start_pos = (start_pos + r[1])
        else:
            start_pos = (start_pos - r[1])
        if old_pos == 0 and r[0] == "L" :
            count -= 1
        count += abs(start_pos // 100) + (start_pos <= 0 and start_pos % 100 == 0)
        start_pos %= 100
    print(count)

def main():
    p1()
    p2()

if __name__ == "__main__":
    main()