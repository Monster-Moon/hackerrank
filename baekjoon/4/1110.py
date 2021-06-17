
n1 = n2 = int(input())


l = 0
while True:
    t = n2 // 10 + n2 % 10
    n2 = n2 % 10 * 10 + t % 10
    l += 1
    if n1 == n2:
        break

print(l)
