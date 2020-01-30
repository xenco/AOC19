p = [int(x) for x in open("in").read().split(",")]

var_input = 5

ip = 0
op_lengths = {
    '1': 4,
    '2': 4,
    '3': 2,
    '4': 2,
    '5': 3,
    '6': 3,
    '7': 4,
    '8': 4,
}

outputs = []


def p_mode(pm, n):
    val = p[ip + n]
    try:
        mode = pm[-n]
    except IndexError:
        mode = "0"

    return val if mode == "1" else p[val]


while True:
    op = int(str(p[ip])[-2:])
    pm = str(p[ip])[:-2]

    mod_ip = True

    if op == 1:  # add
        p1 = p_mode(pm, 1)
        p2 = p_mode(pm, 2)

        print("ADD: %s + %s, TO: %s" % (p1, p2, p[ip + 3]))

        p[p[ip + 3]] = p1 + p2
    elif op == 2:  # mul
        p1 = p_mode(pm, 1)
        p2 = p_mode(pm, 2)

        print("MUL: %s * %s, TO: %s" % (p1, p2, p[ip + 3]))

        p[p[ip + 3]] = p1 * p2
    elif op == 3:  # input
        print("STORE: %s, TO: %s" % (var_input, p[ip + 1]))
        p[p[ip + 1]] = var_input
    elif op == 4:  # output
        p1 = p_mode(pm, 1)
        print("OUTPUT: %s, FROM: %s" % (p1, p[ip + 1]))
        outputs.append(p1)
    elif op == 5:  # jump-if-true
        p1 = p_mode(pm, 1)
        p2 = p_mode(pm, 2)

        if p1:
            ip = p2
            mod_ip = False
    elif op == 6:  # jump-if-false
        p1 = p_mode(pm, 1)
        p2 = p_mode(pm, 2)

        if not p1:
            ip = p2
            mod_ip = False
    elif op == 7:  # less than
        p1 = p_mode(pm, 1)
        p2 = p_mode(pm, 2)

        p[p[ip + 3]] = 1 if p1 < p2 else 0
    elif op == 8:  # equals
        p1 = p_mode(pm, 1)
        p2 = p_mode(pm, 2)

        p[p[ip + 3]] = 1 if p1 == p2 else 0
    elif op == 99 or op not in [1, 2, 3, 4, 99]:
        break

    if mod_ip:
        ip += op_lengths[str(op)]

print("")
print(outputs)
print(",".join([str(x) for x in p]))
