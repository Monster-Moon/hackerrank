
h, m = map(int, input().split(' '))

tmp =  h * 60 + m - 45
minute = tmp + 1440 if tmp < 0 else tmp
print(*[minute // 60, minute % 60])

