n=int(input("enter a number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    if i==n:
        print("factorial of a number is :",fact)
    i=i+1
