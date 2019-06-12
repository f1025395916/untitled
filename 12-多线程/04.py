from collections import  Iterable
from collections import  Iterator
ll =[1,2,3,4,5]
#是可迭代的,但不是迭代器
print(isinstance(ll,Iterable))
print(isinstance(ll,Iterator))

l = [x*x for x in range(5)]
g = (x*x for x in range(5))
print(type(l))
print(type(g))