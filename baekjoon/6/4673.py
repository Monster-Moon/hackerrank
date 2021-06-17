
def num(x):
    return(x + sum([int(i) for i in str(x)]))

cand = list(range(10001))
for i in range(10001):
    tmp = num(i)
    if tmp in cand:
        cand.remove(tmp)
        
print(*cand, sep = '\n')