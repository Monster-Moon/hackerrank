import math


for i in range(int(input())):
    start, end = map(int, input().split(' '))
    diff = end - start
    i_ceil = math.ceil(math.sqrt(diff))
    if diff <= (i_ceil-1) ** 2 + (i_ceil-1):
        print(2 * (i_ceil - 1))
    else:
        print(2 * (i_ceil - 1) + 1)    
