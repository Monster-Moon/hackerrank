s = input()

small = sorted([i for i in s if i.islower() and not i.isdigit()])
big = sorted([i for i in s if i.isupper()])
digit_odd = sorted([i for i in s if i.isdigit() and int(i) % 2 != 0])
digit_even = sorted([i for i in s if i.isdigit() and int(i) % 2 == 0])

print(''.join(small + big + digit_odd + digit_even))
