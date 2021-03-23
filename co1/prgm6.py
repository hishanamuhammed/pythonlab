list=[]
for i in range(2):
    x=input("Enter first name:")
    list.append(x)
print(list)
new=[x for x in list if "a" in x]
print(new)