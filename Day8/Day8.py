with open('data.txt') as r:
    inp = [l.rstrip('\n') for l in r.read().strip().split('\n')]

acc = 0
pc = 0
visited = set()
while True:
    if pc in visited:
        print(acc)
        break
    visited.add(pc)
    line = inp[pc]
    inst, arg = line.split()
    arg = int(arg)

    if inst == 'jmp':
        pc += arg
        continue
    if inst == 'acc':
        acc += arg
    if inst == 'nop':
        pass

    pc += 1

def count(counter):
    acc = 0
    pc = 0
    visited = set()
    while True:
        if pc == len(counter):
            return acc
        if pc in visited:
            return
        visited.add(pc)
        line = counter[pc]
        inst, arg = line.split()
        arg = int(arg)
        if inst == 'jmp':
            pc += arg
            continue
        if inst == 'acc':
            acc += arg
        if inst == 'nop':
            pass

        pc += 1

for i in range(len(inp)):
    counter = inp[:]
    if 'jmp' in counter[i]:
        counter[i] = counter[i].replace('jmp', 'nop')
    else:
        counter[i] = counter[i].replace('nop', 'jmp')
    x = count(counter)
    if x:
        print(x)