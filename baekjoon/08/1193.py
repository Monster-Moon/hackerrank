

inp = int(input())

l = 1
while True:
    s = l * (l+1) / 2 - inp
    if s < 0:
        l +=1
        continue
    else:
        if l % 2 == 1:
            print(1 + int(s), '/', l - int(s), sep = '')
        else:
            print(l - int(s), '/', 1 + int(s), sep = '')
        break

