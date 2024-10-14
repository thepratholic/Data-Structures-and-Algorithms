def function(n):
    if n<=1: return 1
    if n % 2 == 0:
        return function(n//2)
    return function(n//2) + function(n//2+1)
print(function(11))