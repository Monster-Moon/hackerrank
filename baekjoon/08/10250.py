
for _ in range(int(input())):
    h, w, n = map(int, input().split(' '))
    f = str(n % h if n % h != 0 else h)
    g = ('0' + str((n-1)//h + 1) if len(str((n-1) // h + 1)) < 2 else str((n-1)//h + 1))
    print(f + g)
    
