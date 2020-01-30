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

for wire in [0, 1]:
    x = cp[0]
    y = cp[1]

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

            wires[wire]["points"].add(str(x) + ":" + str(y))

intersections = wires[0]["points"].intersection(wires[1]["points"])
min_distance = None

for i in intersections:
    x = int(i.split(":")[0])
    y = int(i.split(":")[1])

    distance = abs(cp[0] - x) + abs(cp[1] - y)
    min_distance = distance if min_distance is None or min_distance > distance else min_distance

print(min_distance)