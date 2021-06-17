

def check(x):
    t = [x[0]]
    for i in range(1, len(x)):
        if x[i] != x[i-1]:
            t.append(x[i])
        else:
            continue
    if len(t) == len(set(t)):
        return(1)
    else:
        return(0)
    
s = 0
for _ in range(int(input())):
    s += check(input())

print(s)