import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)

words = ''.join([item[j] for j in range(m) for item in matrix])
print(re.sub(r'(?<=[a-zA-Z])([%$#\s%]{1,})(?=[a-zA-Z])', ' ', words))
