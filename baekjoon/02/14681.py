
axis = []
for _ in range(2):
    axis.append(float(input()))

if axis[0] > 0:
    if axis[1] > 0:
        print(1)
    else:
        print(4)
else:
    if axis[1] > 0:
        print(2)
    else:
        print(3)