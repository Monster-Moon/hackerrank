
for _ in range(int(input())):
    input_vec = list(map(int, input().split(' ')))
    mean = sum(input_vec[1:]) / input_vec[0]
    print("{0:.3f}".format(sum([i > mean for i in input_vec[1:]])/ input_vec[0] * 100), '%', sep = '')


