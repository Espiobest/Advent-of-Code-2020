r = open('data.txt')
c = r.read().strip().split('\n')
x=0
y=0
for i in c:
    s=i.split()
    a,b=s[0].split('-')
    a,b=map(int,(a,b))

    if s[2].count(s[1][0]) >= a and s[2].count(s[1][0]) <= b: x += 1 #part 1

    if s[2][a-1] == s[1][0] and s[2][b-1] != s[1][0]: y += 1 # part 2
    elif s[2][a-1] != s[1][0] and s[2][b-1] == s[1][0]: y += 1

print(x)
print(y)
