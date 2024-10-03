def fact(n):
    if n==0: return 1
    else: return fact(n-1) * n


def nCr(n,r):
    # code here
    if r > n: return 0
    return fact(n) // (fact(r) * fact(n-r))