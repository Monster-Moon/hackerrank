
max_inx = max_val = 0
for i in range(9):
    n = int(input())
    if n > max_val:
        max_val = n
        max_inx = i + 1
    else:
        continue

print(max_val)
print(max_inx)