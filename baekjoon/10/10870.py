def fibo(x):
    if x <= 1:
        return(x)
    else:
        return(fibo(x-1) + fibo(x-2))

print(fibo(int(input())))

