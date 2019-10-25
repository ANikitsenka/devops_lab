a = int(input())
b = int(input())
result = 0

aa = bin(a)[2:]
bb = bin(b)[2:]

length_a = len(aa)
length_b = len(bb)

if length_a > length_b:
    zs = '0' * (length_a - length_b)
    bb = zs + bb
else:
    zs = '0' * (length_b - length_a)
    aa = zs + aa

for a, b in zip(aa, bb):
    if a != b:
        result += 1
print(result)
