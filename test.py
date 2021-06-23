
import numpy as np
import re

def tmp_fun(i):
    if i > 0:
        return '1'
    elif i < 0:
        return '0'
    else:
        return '2'

arr = [5, 1, 3, 4, 5]
s = ''.join(list(map(tmp_fun, np.diff(arr).tolist())))
        
s_vec = re.findall(r'^[12]{1,}|^[02]{1,}|[12]{1,}$|[02]{1,}$|[12]{0,}10[02]{0,}', s)
