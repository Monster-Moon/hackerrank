
k = 1
x = int(input())
while True:
    if 3*(k**2) - 3*k + 1 < x:
        k += 1
    else:
        break
    
print(k)
