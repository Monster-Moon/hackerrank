
import re

inp = input()
p = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

p_target = [i for i in p if i in inp]

s = 0
for i in p_target:
    s += inp.count(i)
    inp = inp.replace(i, '')



print(s + len(inp))







