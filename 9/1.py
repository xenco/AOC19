p = [int(x) for x in open("in").read().split(",")] + [0] * 100000

var_input = 1

ip = 0

base_pointer = 0

op_lengths = {
    '1': 4,
    '2': 4,
    '3': 2,
    '4': 2,
    '5': 3,
    '6': 3,
    '7': 4,
    '8': 4,
    '9': 2,
}

outputs = []


def p_mode(pm, n, write_mode=False):
    val = p[ip + n]
    try:
        mode = pm[-n]
    except IndexError:
        mode = "0"

    if mode == "0":  # positional
        return p[val], int(mode)
    elif mode == "1":  # value
        return val, int(mode)
    elif mode == "2":  # relational
        return val + base_pointer, int(mode)


while True:
    op = int(str(p[ip])[-2:])
    pm = str(p[ip])[:-2]

    mod_ip = True

    if op == 1:  # add
        p1, mode1 = p_mode(pm, 1)
        p2, mode2 = p_mode(pm, 2)
        p3, mode2 = p_mode(pm, 3, True)

        print("ADD: %s (%s), %s (%s), %s (%s)" % (p1, mode1, p2, mode2, p3, mode3))

        p[p3] = p1 + p2
    elif op == 2:  # mul
        p1, mode1 = p_mode(pm, 1)
        p2, mode2 = p_mode(pm, 2)
        p3, mode3 = p_mode(pm, 3, True)

        print("MUL: %s (%s), %s (%s), %s (%s)" % (p1, mode1, p2, mode2, p3, mode3))

        p[p3] = p1 * p2
    elif op == 3:  # input
        p1, mode = p_mode(pm, 1, True)

        print("STORE: %s, %s (%s)" % (var_input, p1, mode))

        p[p1] = var_input
    elif op == 4:  # output
        p1, mode = p_mode(pm, 1)

        print("OUTPUT: %s, %s" % (p1, p[ip + 1]))

        outputs.append(p1)
    elif op == 5:  # jump-if-true
        p1, mode1 = p_mode(pm, 1)
        p2, mode2 = p_mode(pm, 2, True)

        if p1:
            ip = p2
            mod_ip = False
    elif op == 6:  # jump-if-false
        p1, mode1 = p_mode(pm, 1)
        p2, mode2 = p_mode(pm, 2, True)

        if not p1:
            ip = p2
            mod_ip = False
    elif op == 7:  # less than
        p1, mode1 = p_mode(pm, 1)
        p2, mode2 = p_mode(pm, 2)
        p3, mode3 = p_mode(pm, 3, True)

        p[p3] = 1 if p1 < p2 else 0
    elif op == 8:  # equals
        p1, mode1 = p_mode(pm, 1)
        p2, mode2 = p_mode(pm, 2)
        p3, mode3 = p_mode(pm, 3, True)

        p[p3] = 1 if p1 == p2 else 0
    elif op == 9:  # base
        p1, mode = p_mode(pm, 1)

        print("BASE: %s" % (p1))

        base_pointer += p1
    elif op == 99 or op not in [1, 2, 3, 4, 99]:
        break

    if mod_ip:
        ip += op_lengths[str(op)]

print("")
print(outputs)
print(",".join([str(x) for x in p]))
