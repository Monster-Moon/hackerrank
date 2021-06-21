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
        
n = int(input())
m = int(input())

prime_vec = [i for i in range(n, m+1) if isprime(i)]

if len(prime_vec) == 0:
    print(-1)
else:
    print(sum(prime_vec))
    print(min(prime_vec))

        

    
