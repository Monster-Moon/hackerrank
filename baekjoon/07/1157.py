from collections import Counter

def check(inp):
    inp_counter = Counter(inp.upper())    
    
    max_val = max(inp_counter.values())
    max_inx = [i for i, x in enumerate([i == max_val for i in inp_counter.values()]) if x]
    if len(max_inx) == 1:
        return(list(inp_counter)[max_inx[0]])
    else:
        return('?')
    
print(check(input()))
