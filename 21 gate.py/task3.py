a=[1,2,3,"apple","banana",5,6,7]

print(sum(filter(lambda n:isinstance(n,int),a)))