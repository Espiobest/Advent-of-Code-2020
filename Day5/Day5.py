r = open('data.txt')
c = r.read()

c = c.replace('L','0').replace('F','0').replace('B','1').replace('R','1').split('\n')
ids = [int(i,2) for i in c]
print(max(ids)) #a1

for x in range(min(ids), max(ids)):
    if x not in ids:
        print(x) #a2
        break