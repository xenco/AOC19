p = [int(x) for x in open("in").read().split(",")]
p[1] = 12
p[2] = 2
op = 0

while True:
    if p[op] == 99 or p[op] not in [1, 2]:
        break

    x = p[p[op + 1]]
    y = p[p[op + 2]]
    p[p[op + 3]] = x + y if p[op] == 1 else x * y
    op += 4

print(p[0])
