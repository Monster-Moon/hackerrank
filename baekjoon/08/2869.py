
from math import ceil

a, b, z = map(int, input().split(' '))
print(ceil((z - b) / (a - b)))

