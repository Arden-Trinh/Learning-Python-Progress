a,b,c=[int(x) for x in input().split()]
if a==0:
    if b==0:
        if c==0:
            print("INF")
        else:
            print("NO")
    else:
        print("{:.2f}".format(-c/b))
else:
    delta=(b**2)-(4*a*c)
    if delta<0:
        print("NO")
    elif delta==0:
        x=-b/(2*a)
        print("{:.2f}".format(x))
    else:
        x1=(-b-(delta**(1/2)))/(2*a)
        x2=(-b+(delta**(1/2)))/(2*a)
        
