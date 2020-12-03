from itertools import permutations


with open('data.txt','r') as r:
  c = r.read().strip().split()

numbers = [*map(int,c)]
target_number = 2020

nums1 = (list(permutations(numbers, 2)))

result1 = [i for i in nums if i[0]+i[1] == target_number] #part 1
print(result1)

nums2 = (list(permutations(numbers, 3)))

result2 = [i for i in nums if i[0]+i[1]+i[2] == target_number] #part 2
print(result2)
