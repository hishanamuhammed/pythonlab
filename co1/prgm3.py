list=[1,-3,5,-5,4,8,6]
newlist=[x for x in list if x>0]
print(newlist)

N=int(input("Enter number of no:s "))
list=[]
for x in range(N):
  x=int(input("Enter no: "))
  list.append(x)
print(list)
squarelist=[x**2 for x in list]
print(squarelist)


word="umberella"
vowels="aeiou"
list=[x for x in word if x in vowels]
print(list)


word="flower"
list=[ord(x) for x in word]