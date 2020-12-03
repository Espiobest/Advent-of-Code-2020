with open('data.txt','r') as r:
    F = r.read().strip().split()
   
lst = [[1,1], [3,1], [5,1], [7,1], [1,2]]
k = 1
for a,b in lst:
    z = c = s = 0
    while z < len(F):
        c += a
        z += b
        if F[z][c%len(F[z])]== '#' and z<len(F):
            s+=1
    k *= s
    if a == 3 and b == 1:
        print(s)
print(k)
