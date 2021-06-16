
for i in range(int(input())):
    input()
    input_seq = list(map(int, input().split(' ')))
    min_inx = int(input_seq.index(min(input_seq)))
    cond1 = input_seq[:min_inx] == sorted(input_seq[:min_inx], reverse = True)
    cond2 = input_seq[min_inx+1:] == sorted(input_seq[min_inx+1:], reverse = False)    
    if cond1 and cond2:
        print('Yes')
    else:
        print('No')

