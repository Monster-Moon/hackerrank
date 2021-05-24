# Solution 1
import os

def solve(s):
    s_vec = s.split(' ')
    return(' '.join([i.capitalize() for i in s_vec]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

## Solution 2
def solve(s):
    s_vec = s.split(' ')    
    word = []
    for i in s_vec:
        word.append(''.join([i[j].upper() if j == 0 else i[j] for j in range(len(i))]))

    return(' '.join(word))








