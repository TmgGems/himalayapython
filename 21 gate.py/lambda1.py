#map,filter

#map(funcn,iterable)
a=[1,6,3,4,5]
output=[]
# for i in a:
#     output.append(i+1)

# print(output)
            #USING MAP
# def increment_by_one(n):
#     return n+1

#output=map(increment_by_one,a)
#print(list(output))
#           OR
output=map(lambda n:n+1,a)
print(list(output))