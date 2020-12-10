with open("data.txt") as f:
    s = f.read().strip().split("\n")

data = [*map(int,s)]


def valid(nums, n):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == n:
                return True
    return False


for i in range(25,len(data)):
    if not valid(data[i-25:i], data[i]):
     num = data[i]
     print(num)
     break

d = {}
s = 0

for i in range(len(data)):
    d[s] = i
    s += data[i]
    if s - num in d:
        v = data[d[s-num]:i+1]
        print(min(v)+max(v))
        break