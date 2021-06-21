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
        
input()
num_vec = map(int, input().split(' '))
print(sum(list(map(isprime, num_vec))))
        

    
