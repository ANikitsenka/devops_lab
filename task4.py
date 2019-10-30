N = int(input())
cmd = []
men_s = 0
iterator = 0

for i in range(N):
    cmd_read = [int(i) for i in input().split()]
    cmd += cmd_read

men = cmd[1::2]
for j in range(len(men)):
    men_s += men[j]

if men_s <= 0:
    print('-1')
else:
    while iterator <= len(cmd) / 2:
        ages = cmd[::2]
        oldest = max(ages)
        if cmd[cmd.index(oldest) + 1] == 0:
            check = cmd.index(oldest)
            cmd[check] = 0
        else:
            print(cmd.index(oldest))
            break
