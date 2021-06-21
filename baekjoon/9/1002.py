
from math import sqrt

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    d_list = [r1, r2, d]
    d_max = max(d_list)
    d_list.remove(d_max)
    
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == r1 + r2 or d_max == sum(d_list):
            print(1)
        elif d_max > sum(d_list):
            print(0)
        else:
            print(2)
    