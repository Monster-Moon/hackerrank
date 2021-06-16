import re

N = int(input())
for i in range(N):
    print(re.sub(r'(?<=\s)&&(?=\s)', 'and', re.sub(r'(?<=\s)\|\|(?=\s)', 'or', input())))
