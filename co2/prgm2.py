a=0
b=1
n=int(input("enter the terms:"))
if n<=0:
    print("febnocci series are")
elif n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)
