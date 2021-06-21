while True:
    num_vec = sorted(list(map(int, input().split(' '))))
    if 0 in num_vec:
        break
    
    if num_vec[2] ** 2 == num_vec[1] ** 2 + num_vec[0] ** 2:
        print('right')
    else:
        print('wrong')