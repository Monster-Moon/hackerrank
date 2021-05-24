def minion_game(string):
    # your code goes here
    vowels = 'aeiou'.upper()
    
    l = len(string)
    kevin = sum(l-i for i in range(l) if string[i] in vowels)
    stuart = l*(l + 1)/2 - kevin
    
    if kevin == stuart:
        print ('Draw')
    elif kevin > stuart:
        print ('Kevin %d' % kevin)
    else:
        print ('Stuart %d' % stuart)    
        
if __name__ == '__main__':
    s = input()
    minion_game(s)