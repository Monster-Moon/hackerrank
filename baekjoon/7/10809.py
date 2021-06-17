alpha = 'abcdefghijklmnopqrstuvwxyz'

def check(x, a):
    tmp = [x == i for i in a]
    if sum(tmp) == 0:
        return(-1)
    else: 
        return([i for i, y in enumerate(tmp) if y][0])

inp = input()
print(*[check(i, inp) for i in alpha])