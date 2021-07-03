a,b,c,e,f,g=[int(x) for x in input().split()]
if (a/e)!=(b/f):
    y=((a*g)-(e*c))/((f*a)-(b*e))
    x=(c-(b*y))/a
    if y==0:
        y=abs(y)
    print("{:.2f}".format(x),end=" ")
    print("{:.2f}".format(y))
elif (a/e)==(b/f) and (a/e)!=(c/g) and (b/f)!=(c/g):
    print("VONGHIEM")
elif (a/e)==(b/f) and (a/e)==(c/g) and (b/f)==(c/g):
    print("VOSONGHIEM")