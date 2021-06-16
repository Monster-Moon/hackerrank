from itertools import product

n, M = map(int, input().split())
num_vec = []
for _ in range(n):
    input_vec = map(int, input().split(' ')[1:])
    num_vec.append(list(set(input_vec)))

result = map(lambda x: sum([j ** 2 for j in x]) % M, product(*num_vec))
print(max(result))

