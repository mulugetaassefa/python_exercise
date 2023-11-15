# list orderd, diplicate ,mutable, changeable
myList =["banana","mango","apple"]

print(myList)

item= myList[0:1]
print(item)

print(len(myList))

for i in myList:
    print(i)

if "banana" in myList:
    print("yes")
else:
    print("no")

# append value to list
myList.append("lemon")
print(myList)
# pop value
myList.pop(-1)
print(myList)
# inser value
myList.insert(0,"karrot")
print(myList)
# clear() clear all value
# reverse() reverse all value


# sort 3
myList = [2,4,7,8,-1,9]
item =sorted(myList)
print(item)

myList2 =[0] * 5
print(myList2)
# list concatination
new_List = myList + myList2
print(new_List)
# copy()

myList3 =[1,2,3,4,5]
b =[i*i for i   in myList3]
print(myList)
print(b)