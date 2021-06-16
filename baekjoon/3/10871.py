
_, n = map(int, input().split(' '))
num = list(map(int, input().split(' ')))
print(*[i for i in num if i < n])