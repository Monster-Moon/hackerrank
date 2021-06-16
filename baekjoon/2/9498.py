
score = int(input())
score_dic = {'A' : [90, 100], 'B': [80, 89], 'C': [70, 79], 'D': [60, 69], 'F': [0, 59]}
print([i[0] for i in score_dic.items() if score >= i[1][0] and score <= i[1][1]][0])

