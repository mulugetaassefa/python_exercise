# lambda argument : expression
from functools import reduce
add10 = lambda x: x + 10
print(add10(5))

multi = lambda x,y: x*y
print(multi(4,6))


point2d =[(2,4),(5,7),(-1,6),(5,2),(-4,3)]
print(point2d)
sortedpoint2d = sorted(point2d, key =lambda x: x[1])
print(sortedpoint2d)

# map(fun, seq)
a =[1,2,3,4,5]
b =map(lambda x: x*2,a)
print(list(b))

# same above code as
c = [x*2 for x in a]
print(c)

# filter method

c =[2,3,5,6,7,9]
d =filter(lambda x: x %2==0,a)
print(list(d))

# reduce method

a =[1,2,3,4,5]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
