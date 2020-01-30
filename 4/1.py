min = int(open("in").read().split("-")[0])
max = int(open("in").read().split("-")[1])


def is_valid_password(n):
    if len(str(n)) != 6:
        return False

    if n < min or n > max:
        return False

    has_double = False
    for i, v in enumerate(str(n)):
        if i > 0:
            if str(n)[i] == str(n)[i - 1]:
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


valid_passwords = len([x for x in range(min, max + 1) if is_valid_password(x)])
print(valid_passwords)
