from itertools import combinations

n, items, c = int(input()), input().split(' '), int(input())
comb_list = list(combinations(items, c))
con_a = [j for j in comb_list if 'a' in j]

print(len(con_a)/len(comb_list))