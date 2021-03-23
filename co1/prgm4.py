s=str(input("enter the string:"))
words=s.split()
count=dict()
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)