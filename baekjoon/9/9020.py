
from math import sqrt
import sys

def isprime(x):
    s = True
    if x == 1:
        s = False
    elif x == 2:
        s = True
    elif x % 2 == 0:
        s = False
    else:    
        for i in range(3, int(sqrt(x)) + 2, 2):
            if x % i == 0:
                s = False
                break
    return(s)    

prime_list = [i for i in range(2, 10000) if isprime(i)]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    for i in range(n // 2, n-1):
        if i in prime_list and n-i in prime_list:
            print(n-i, i)
            break
        else:
            continue
        