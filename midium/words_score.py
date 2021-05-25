def score_words(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    v_count = list(map(lambda x: sum([y in vowels for y in x]), words))
    return(sum([2 if v % 2 == 0 else 1 for v in v_count]))
    
n = int(input())
words = input().split()
print(score_words(words))