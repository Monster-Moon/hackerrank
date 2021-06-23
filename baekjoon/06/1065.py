n = int(input())

def han(i):
    tmp = [int(j) for j in str(i)]
    if len(tmp) == 1:
        return(1)
    else:
        return(len(set([i - j for i, j in zip(tmp[1:], tmp[:-1])])))

print(len([i for i in range(n+1) if han(i) == 1])-1)


