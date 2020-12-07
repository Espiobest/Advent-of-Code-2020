import collections
import re

r = open('data.txt')

lines = [l.strip('\n') for l in r.read().strip().split('\n')]

bags = collections.defaultdict(set)
has_bag = collections.defaultdict(list)

for line in lines:
    color = re.match(r'(.+?) bags contain', line)[1]
    for ct, incolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
        bags[incolor].add(color)
        has_bag[color].append([int(ct), incolor])


#part 1
def check(name):
    s = bags[name].copy()
    for bag in bags[name]:
        s.update(check(bag))
    return s


print(len(check('shiny gold')))

#part 2
def cost(color):
    total = 0
    for ct, bag in has_bag[color]:
        total += ct
        total += ct * cost(bag)
    return total


print(cost('shiny gold'))

