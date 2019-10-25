N = int(input())
task_list = []
cmd = []
j = 0


def _insert(index, e):
    task_list.insert(index, int(e))


def _print():
    print(task_list)


def _remove(e):
    task_list.remove(int(e))


def _append(e):
    task_list.append(int(e))


def _pop():
    task_list.pop()


def _sort():
    task_list.sort()


def _reverse():
    task_list.reverse()


for i in range(N):
    cmd_read = [str(i) for i in input().split()]
    cmd += cmd_read


while j <= (len(cmd) - 1):
    if cmd[j] == 'insert':
        _insert(int(cmd[j + 1]), cmd[j + 2])
        j += 3
        continue
    if cmd[j] == 'print':
        _print()
        j += 1
        continue
    elif cmd[j] == 'remove':
        _remove(cmd[j + 1])
        j += 2
        continue
    elif cmd[j] == 'append':
        _append(cmd[j + 1])
        j += 2
        continue
    elif cmd[j] == 'pop':
        _pop()
        j += 1
        continue
    elif cmd[j] == 'sort':
        _sort()
        j += 1
        continue
    elif cmd[j] == 'reverse':
        _reverse()
        j += 1
        continue
