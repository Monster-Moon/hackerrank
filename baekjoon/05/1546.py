
n = int(input())
input_vec = list(map(int, input().split(' ')))

print(sum([i * 100 / max(input_vec) for i in input_vec])/n)