#RANGE
abc=list(range(5))
print(abc)
abc=list(range(1,6))
print(abc)


#SET
abd=[5,4,2,10,20,2,2,5,7]
print(abd)
print(set(abd))
list(set(abd))
print(abd.count(2))

#MIN,MAX,SUM
print(min(abd))
print(max(abd))
print(sum(abd))

#copy
abd=[5,4,3,2,1]
print(abd)
abd1=abd.copy()
print(abd1)
abd2=abd1
print(abd2)
print(id(abd1))
print(id(abd2))
print(id(abd))
abd3=abd
print(id(abd3))

#Concatenate
abd=[5,4,7,8]
print(abd)
abd1=[1,2]
print(abd1)
print(abd+abd1)


#Append
abd=[5,4,2]
abd.append(7)
print(abd)
my=[10,20]
abd.append(my)
print(abd)
#append data will add your containt at the end of your list.

#Extend
abd=[5,4,2]
my=[10,20]
abd.extend(my)
print(abd)

