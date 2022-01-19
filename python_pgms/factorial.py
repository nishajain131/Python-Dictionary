#Method1. using recursion

def fact(n):
    if n<=1:
        return 1
    else:
        res = n*fact(n-1)
    return res
ans = fact(3)
print(ans)

#Method2. without recursion

n=3
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)