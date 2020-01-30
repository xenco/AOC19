cp = [0, 0]

wires = [
    {
        "dirs": open("in").readlines()[0].split(","),
        "points": set([])
    },
    {
        "dirs": open("in").readlines()[1].split(","),
        "points": set([])
    }
]

intersections = []
intersection_steps = [
    {},
    {}
]

for wire in [0, 1]:
    x = cp[0]
    y = cp[1]

    steps_total = 0

    for d in wires[wire]["dirs"]:
        for i in range(int(d[1:])):
            if d[0] == "L":
                x -= 1
            elif d[0] == "R":
                x += 1
            elif d[0] == "U":
                y -= 1
            elif d[0] == "D":
                y += 1

            steps_total += 1

            id = str(x) + ":" + str(y)
            wires[wire]["points"].add(id)
            if id not in intersection_steps[wire]:
                intersection_steps[wire][id] = steps_total

intersections = wires[0]["points"].intersection(wires[1]["points"])

min_steps = None

for i in intersections:
    x = int(i.split(":")[0])
    y = int(i.split(":")[1])
    id = str(x) + ":" + str(y)

    steps = intersection_steps[0][id] + intersection_steps[1][id]
    min_steps = steps if min_steps is None or min_steps > steps else min_steps

print(min_steps)