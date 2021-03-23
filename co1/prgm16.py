str1="hello"
str2="world"
a=list(str1)
b=list(str2)
temp=a[1]
a[1]=b[1]
b[1]=temp
print("swapping the character at position 1:","".join(a),"".join(b))
