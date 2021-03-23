import csv
header = ["place", "name", "age"]
with open('city.csv',"w") as csvfile:
    write = csv.DictWriter(csvfile,fieldnames=header)
    write.writeheader()
    write.writerow({"place": "vatakara", "name": "Samuel", "age": 21})
    write.writerow({"place": "kainatty", "name": "Aswanth", "age": 21})
    write.writerow({"place": "Tholikkode", "name": "Rojin", "age": 23})
    write.writerow({"place": "Palakkaadu", "name": "Aleena", "age": 13})
with open("city.csv") as csvfile:
    read= csv.DictReader(csvfile)
    n=input("enter the colomn name you want:")
    for i in read:
        print(i[n])
