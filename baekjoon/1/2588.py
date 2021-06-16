
a = int(input())
b = input()

return_vec = [a * int(i) for i in b]
return_vec.reverse()
return_vec.append(a * int(b))

for r in return_vec:
    print(r)


