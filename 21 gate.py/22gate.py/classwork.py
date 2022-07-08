
heros=["spider man","thor","hulk","iron man","captain america"]
#1.
# i=0
# for x in heros:
#     i=i+1
# print(i)
print(len(heros))
#2.
heros.append("black panther")
print(heros)
heros.remove("black panther")
#3.
heros.insert(3,"black panther")
print(heros)
#4.
heros[1:3]=["Doctor Strange"]
print(heros)
#5.
heros.sort()
print(heros)