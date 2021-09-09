n=int(input())
a,b=[int(x) for x in input().split()]
if n%a==0 and n%b==0:
    print("Co, tat ca!")
elif n%a==0 and n%b!=0:
    print("Chi chia het cho",a,end=",")
elif n%a!=0 and n%b==0:
    print("Chi chia het cho",b,end=".")
else: 
    print("Khong chia het cho so nao ca.")
