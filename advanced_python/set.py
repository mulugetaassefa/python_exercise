# unordered, mutable , no duplicates

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.pop()
for i in myset:
    print(i)
print(myset)


if 7 in myset:
    print("yes")
else:
  print("no")

  # union and intersection

odds = {1,3,5,7,9}
evens =  {0,2,4,6,8}
primes = {2,3,5,7,11}
u = odds.union(evens)
print(u)
v = u.union(primes)
print(v)
 
# intersection of even and odd is empty
i = odds.intersection(evens)
print(i)