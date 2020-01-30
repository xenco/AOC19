sum = 0

for x in open("in").readlines():
    while True:
        fuel_sum = int(int(x) / 3) - 2

        if fuel_sum <= 0:
            break

        sum += fuel_sum
        x = fuel_sum

print(sum)