def demsouoc(a):
    a=abs(a)
    dem=0
    for i in range(1,a+1):
        if a%i==0:
            dem+=1 
    return dem
a=int(input())
print(demsouoc(a))

