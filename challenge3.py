#num=[]
#for i in range(1,51):
 #   if i%4==0:
#        num.append(i)
#print(sum(num))
# OR
#print(sum(range(4,51,4)))
#OR
total=sum([i for i in range(1,51) if i%4==0])
print(total)