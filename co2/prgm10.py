n=int(input("enter the limit"))
print("factors are")
for i in range(1,n+1):
    if n%i==0:
        print(i)
