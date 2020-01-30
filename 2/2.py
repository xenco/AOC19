import random

p_in = [int(x) for x in open("in").read().split(",")]

while True:
    p = p_in.copy()
    p[1] = random.randint(0, 99)
    p[2] = random.randint(0, 99)
    op = 0

    while True:
        if p[op] == 99 or p[op] not in [1, 2]:
            break

        x = p[p[op + 1]]
        y = p[p[op + 2]]
        p[p[op + 3]] = x + y if p[op] == 1 else x * y
        op += 4

    if p[0] == 19690720:
        print(str(100 * p[1] + p[2]))
        break
