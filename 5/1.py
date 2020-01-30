p = [int(x) for x in open("in").read().split(",")]

var_input = 1

ip = 0
op_lengths = {
    '1': 4,
    '2': 4,
    '3': 2,
    '4': 2,
}

outputs = []


while True:
    op = int(str(p[ip])[-2:])
    pm = str(p[ip])[:-2]

    if op == 1:
        # add
        p1 = p[ip + 1]
        try:
            p1_m = pm[-1]
        except IndexError:
            p1_m = "0"

        p2 = p[ip + 2]
        try:
            p2_m = pm[-2]
        except IndexError:
            p2_m = "0"

        val_p1 = p1 if p1_m == "1" else p[p1]
        val_p2 = p2 if p2_m == "1" else p[p2]

        print("ADD: %s + %s, TO: %s" % (val_p1, val_p2, p[ip + 3]))

        p[p[ip + 3]] = val_p1 + val_p2
    elif op == 2:
        # mul
        p1 = p[ip + 1]
        try:
            p1_m = pm[-1]
        except IndexError:
            p1_m = "0"

        p2 = p[ip + 2]
        try:
            p2_m = pm[-2]
        except IndexError:
            p2_m = "0"

        val_p1 = p1 if p1_m == "1" else p[p1]
        val_p2 = p2 if p2_m == "1" else p[p2]

        print("MUL: %s * %s, TO: %s" % (val_p1, val_p2, p[ip + 3]))

        p[p[ip + 3]] = val_p1 * val_p2
    elif op == 3:
        # store INPUT at p1
        print("STORE: %s, TO: %s" % (var_input, p[ip + 1]))
        p[p[ip + 1]] = var_input
    elif op == 4:
        # print value at p1
        p1 = p[p[ip + 1]]
        print("OUTPUT: %s, FROM: %s" % (p1, p[ip + 1]))
        outputs.append(p1)
    elif op == 99 or op not in [1, 2, 3, 4, 99]:
        break

    ip += op_lengths[str(op)]

print("")
print(outputs)
print(",".join([str(x) for x in p]))