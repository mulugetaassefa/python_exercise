# collection of value ,unchangeable or inmutable, ordered
mytuble = ("max",28,"botson")
print(mytuble)

for x in mytuble:
     print(x)
if "max" in mytuble:
    print("yes")
else:
    print("no")

# change list to tuble and back
my_tuple=('a','p','p','l','e')

my_list =list(my_tuple)
print(my_list)
my_tuple2=tuple(my_list)
print(my_tuple2)


my_list2 ="mule",23,"assosa"
name,age,city=my_list2
print(name)
print(age)
print(city)