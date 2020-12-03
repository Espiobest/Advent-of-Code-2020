with open('data.txt','r') as r:
    inp = r.read().strip().split()
x = 0
y = 0
for i in inp:
    line = i.split()
    start, end = line[0].split('-')
    start, end = map(int,(start, end))

    if start <= line[2].count(line[1][0]) <= end: x += 1 #part 1

    if line[2][start-1] == line[1][0] and line[2][end-1] != line[1][0]: y += 1 # part 2
    elif line[2][start-1] != line[1][0] and line[2][end-1] == line[1][0]: y += 1

print(x)
print(y)
