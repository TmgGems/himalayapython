#tuple is immutable
#a=(1,2,3,1)
#print(a.index(1))
#differnece between list and tuple
from sys import getsizeof
# a=[]
# b=tuple()
# print(getsizeof(a))
# print(getsizeof(b))
a=[1,2,3,4]
b=(1,2,3,4)
print(getsizeof(a))
print(getsizeof(b))