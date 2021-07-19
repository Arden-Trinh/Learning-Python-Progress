a,b,c= [int(x) for x in input().split()]
if a+b>c and a+c>b and b+c>a:
    circumference=a+b+c
    hc=(a+b+c)/2
    area= (hc*(hc-a)*(hc-b)*(hc-c))**(1/2)
    print(circumference,"{:.2f}".format(area))
else:
    print("NO")
