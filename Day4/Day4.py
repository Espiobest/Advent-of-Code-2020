a1 = 0
a2 = 0

with open('data.txt', 'r') as r:
    lines = r.read().split('\n\n')

for line in lines:
    p = {}
    for pas in line.split():
        k,v = pas.split(':')
        p[k] = v
    if 'cid' in p.keys():
        p.pop('cid')
    if len(p) == 7:
        a1 += 1
    else:
        continue

    valid = True
    if not 1920 <= int(p['byr']) <= 2002:
        valid = False
    if not 2010 <= int(p['iyr']) <= 2020:
        valid = False
    if not 2020 <= int(p['eyr']) <= 2030:
        valid = False

    ht = p['hgt']
    if ht.endswith('in') and not 59 <= int(ht[:-2]) <= 76:
        valid = False
    elif ht.endswith('cm') and not 150 <= int(ht[:-2]) <= 193:
        valid = False

    hcl = p['hcl']
    if hcl[0] != '#':
        valid = False

    ecl = p['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid = False

    pid = p['pid']
    if len(pid) != 9:
        valid = False

    if valid:
        a2 += 1

print(a1)
print(a2)

