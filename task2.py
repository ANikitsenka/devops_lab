a = input()
b = input()

if int(a) > 0:
    a = sorted(a, reverse=True)
    for i in range(len(a)):
        a[i] = int(a[i])
    a_out = sum(d * 10 ** i for i, d in enumerate(a[::-1]))
else:
    a = a.replace('-', '')
    a = sorted(a)
    if a[0] == '0':
        a.insert(2, '0')
    for i in range(len(a)):
        a[i] = int(a[i])
    a_out = - sum(d * 10 ** i for i, d in enumerate(a[::-1]))

if int(b) > 0:
    b = sorted(b)
    if b[0] == '0':
        b.insert(2, '0')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    b_out = sum(d * 10 ** i for i, d in enumerate(b[::-1]))
else:
    b = b.replace('-', '')
    b = sorted(b, reverse=True)
    for i in range(0, len(b)):
        b[i] = int(b[i])
    b_out = - sum(d * 10 ** i for i, d in enumerate(b[::-1]))

print(a_out - b_out)
