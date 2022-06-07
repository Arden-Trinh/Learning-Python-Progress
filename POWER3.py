a=int(input())
for i in range (a):
    n=int(input())
    x=round(n**(1/3))
    if x**3==n:
        print("YES")
    else:
        print("NO")
