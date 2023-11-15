#unorder,mutable, no diplication value
mydict ={"name":"jhon","age":20,"city":"assosa"}
print(mydict)
print(mydict["name"])

# create dictionary using dict function
mydict2 =dict(name="tizazu", age=25, city="assosa")
print(mydict2)


   # add value 
mydict2["email"]="mule@gmail.com"
print(mydict2)


#  del value
del mydict2["name"]
print(mydict2)

 # try and catch
try:
    print(mydict2["name"])
except:
    print("error")

for key in mydict2:
    print(key)
for value in mydict2.values():
    print(value)


    for key,value in mydict2.items():
        print(key,value)

        # concatination in dictionary

my_dict = {"name": "abebe","age":20, "city": "addis"}
my_dict2 = {"email":"ab@gmail.com", "addres": "mixico"}
my_dict.update(my_dict2)
print(my_dict)