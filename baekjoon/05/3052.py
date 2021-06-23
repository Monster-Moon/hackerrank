
num_dict = {}
for _ in range(10):
    inp = int(input()) % 42
    if inp in num_dict.keys():
        num_dict[inp] += 1
    else:
        num_dict.update({inp: 1})

print(len(num_dict.keys()))

