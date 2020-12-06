r = open('data.txt')
lines = [*r.read().split('\n\n')]
a1 = 0
a2 = 0

# part 1:
for line in lines:
    line = line.replace('\n','')
    a1 += len(set(line))
print(a1)

# part 2:
for line in lines:
    group = [set(x) for x in line.split('\n')]
    person = group[0]
    for i in group:
        person &= set(i)
    a2 += len(person)
print(a2)