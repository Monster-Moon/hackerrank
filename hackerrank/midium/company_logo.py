if __name__ == '__main__':
    s = list(input())
    d = {}
    for i in s:
        if i not in d.keys():
            d.update({i : 1})
        else:
            d[i] += 1
   
    for char, n in sorted(d.items(), key=lambda c: (-c[1], c[0]))[:3]:
        print(char, n)

