def is_valid_password(n, min, max):
    if len(str(n)) != 6:
        return False

    if n < min or n > max:
        return False

    has_double = False
    double_counts = {}
    for i, v in enumerate(str(n)):
        if i > 0:
            if str(n)[i] == str(n)[i - 1]:
                if not str(n)[i] in double_counts:
                    double_counts[str(n)[i]] = 0
                double_counts[str(n)[i]] += 1

    for k in double_counts:
        if double_counts[k] == 1:
            has_double = True
            break

    if not has_double:
        return False

    is_increasing = True
    for i, v in enumerate(str(n)):
        if i > 0:
            is_increasing = int(str(n)[i]) >= int(str(n)[i - 1])
            if is_increasing is False:
                break

    if not is_increasing:
        return False

    return True

range_min, range_max = int(open("in").read().split("-")[0]), int(open("in").read().split("-")[1])
print(len([x for x in range(range_min, range_max + 1) if is_valid_password(x, range_min, range_max)]))
