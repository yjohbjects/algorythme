# B10872 팩토리얼

def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return(n * (fac(n-1)))

N = int(input())
print(fac(N))
