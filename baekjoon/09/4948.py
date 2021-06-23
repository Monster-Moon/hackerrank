
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


prime_list = [i for i in range(2, 123456 * 2) if isprime(i)]
n = int(sys.stdin.readline())            
while n != 0:
    count = 0
    for i in prime_list:
        if n < i <= n * 2:
            count += 1
    
    print(count)    
    n = int(sys.stdin.readline())    
