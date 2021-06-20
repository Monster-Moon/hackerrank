
inp = int(input())

s = -1
for i in range(inp // 3 + 1):
    x = (inp - 3 * i)
    if x % 5 == 0:
        s = x // 5 + i
        break
    else:
        continue

print(s)
