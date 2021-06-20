
def cumsum(x):
    return([sum(x[:(i+1)]) for i in range(len(x))])

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    n_list = list(range(1, n + 1))
    for i in range(k):
        n_list = cumsum(n_list)

    print(n_list[-1])
    
