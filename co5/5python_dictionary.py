import csv
header=["place","name","age"]
with open("city.csv","w") as csvfile:
    write=csv.DictWriter(csvfile,fieldnames=header)
    write.writeheader()
    limit = int(input("Enter the No.of lines you want to enter:"))
    for i in range(limit):
        row_str = input("Enter the data in order (place,name,age) separated by comma:")
        row_lst = row_str.split(",")
        write.writerow({"place":row_lst[0],"name":row_lst[1],"age":row_lst[1]})
with open("city.csv","r") as csvfile:
    read=csv.DictReader(csvfile)
    for i in read:
        print(dict(i))