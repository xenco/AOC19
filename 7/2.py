import itertools


class IntcodeInterpreter:
    def __init__(self, p, var_inputs):
        self.p = p
        self.var_inputs = var_inputs
        self.var_inputs_processed = 0
        self.ip = 0
        self.op_lengths = {
            '1': 4,
            '2': 4,
            '3': 2,
            '4': 2,
            '5': 3,
            '6': 3,
            '7': 4,
            '8': 4,
        }
        self.outputs = []
        self.halt = False

    def set_signal(self, signal):
        self.var_inputs[1] = signal
        self.var_inputs_processed = 1

    def p_mode(self, pm, n):
        val = self.p[self.ip + n]
        try:
            mode = pm[-n]
        except IndexError:
            mode = "0"

        return val if mode == "1" else self.p[val]

    def calc(self):
        while True:
            op = int(str(self.p[self.ip])[-2:])
            pm = str(self.p[self.ip])[:-2]

            mod_ip = True

            if op == 1:  # add
                p1 = self.p_mode(pm, 1)
                p2 = self.p_mode(pm, 2)

                # print("ADD: %s + %s, TO: %s" % (p1, p2, self.p[self.ip + 3]))

                self.p[self.p[self.ip + 3]] = p1 + p2
            elif op == 2:  # mul
                p1 = self.p_mode(pm, 1)
                p2 = self.p_mode(pm, 2)

                # print("MUL: %s * %s, TO: %s" % (p1, p2, self.p[self.ip + 3]))

                self.p[self.p[self.ip + 3]] = p1 * p2
            elif op == 3:  # input
                print("STORE: %s, TO: %s" % (self.var_inputs[self.var_inputs_processed], self.p[self.ip + 1]))
                self.p[self.p[self.ip + 1]] = self.var_inputs[self.var_inputs_processed]
                self.var_inputs_processed += 1
                if self.var_inputs_processed > 1:
                    self.var_inputs_processed = 0
            elif op == 4:  # output
                p1 = self.p_mode(pm, 1)
                # print("OUTPUT: %s, FROM: %s" % (p1, self.p[self.ip + 1]))
                self.outputs.append(p1)
            elif op == 5:  # jump-if-true
                p1 = self.p_mode(pm, 1)
                p2 = self.p_mode(pm, 2)

                if p1:
                    self.ip = p2
                    mod_ip = False
            elif op == 6:  # jump-if-false
                p1 = self.p_mode(pm, 1)
                p2 = self.p_mode(pm, 2)

                if not p1:
                    self.ip = p2
                    mod_ip = False
            elif op == 7:  # less than
                p1 = self.p_mode(pm, 1)
                p2 = self.p_mode(pm, 2)

                self.p[self.p[self.ip + 3]] = 1 if p1 < p2 else 0
            elif op == 8:  # equals
                p1 = self.p_mode(pm, 1)
                p2 = self.p_mode(pm, 2)

                self.p[self.p[self.ip + 3]] = 1 if p1 == p2 else 0
            elif op == 99 or op not in [1, 2, 3, 4, 99]:
                break

            if mod_ip:
                self.ip += self.op_lengths[str(op)]
        return int(self.outputs[0])


programs = {}
for p in [5, 6, 7, 8, 9]:
    programs[p] = IntcodeInterpreter([int(x) for x in open("in").read().split(",")], [p, 0])

max_output = 0
for perm in list(itertools.permutations([5, 6, 7, 8, 9])):
    o = 0
    while True:
        halt_states = []
        for i in perm:
            o_in = o
            programs[i].set_signal(o)
            o = programs[i].calc()

            print("Start %s with input: %s ==> output: %s, halt: %s" % (i, o_in, o, programs[i].halt))

            halt_states.append(programs[i].halt)

        if o > max_output:
            max_output = o

        if all(halt_states) is True:
            break

print(max_output)
