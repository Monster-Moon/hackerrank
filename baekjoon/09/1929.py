from math import sqrt

def isprime(x):
    s = True
    if x == 1:
        s = False
    else:    
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                s = False
                break
    return(s)    
        
a, b = map(int, input().split(' '))
print(*[i for i in range(a, b+1) if isprime(i)], sep = '\n')

        