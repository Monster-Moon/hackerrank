## Solution 1
dict1 = dict()
for i in range(int(input())):
    word = input()
    if not word in dict1.keys():
        dict1.update({word : 1})
        continue
    dict1[word] += 1

print(len(dict1.keys()))
print(*dict1.values())

## Solution 2
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())



