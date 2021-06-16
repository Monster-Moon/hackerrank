def merge_the_tools(string, k):
    str_list = [list(string[i:(i+k)]) for i in range(0, len(string) + 1, k)]
    for c in str_list:
        tmp_list = []
        for j in c:
            if j not in tmp_list:
                tmp_list.append(j)
        
        print(''.join(tmp_list))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

