list = []
for i in range(6):
    x = int(input("Enter the number:"))
    if x <= 100:
        list.append(x)
    else:
        list.append("over")
print(list)