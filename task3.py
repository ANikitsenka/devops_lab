def convert(x, y):
    a1 = bin(x)[2:]
    b1 = bin(y)[2:]
    return a1, b1


def length(x, y):
    a2 = len(x)
    b2 = len(y)
    return a2, b2


def justice(w, x, y, z):
    if w > x:
        zs = '0' * (w - x)
        z = zs + z
    else:
        zs = '0' * (x - w)
        y = zs + y
    return y, z


def destination(w, x, y, z):
    res = 0
    for w, x in zip(y, z):
        if w != x:
            res += 1
    return res


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    aa, bb = convert(a, b)
    length_a, length_b = length(aa, bb)
    aa, bb = justice(length_a, length_b, aa, bb)
    print(destination(a, b, aa, bb))
