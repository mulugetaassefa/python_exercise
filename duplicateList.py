numbers=[1,2,3,4,5,6,7,3,5]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)