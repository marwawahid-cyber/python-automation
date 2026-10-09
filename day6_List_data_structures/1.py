abd=[1,3,5,8]
print(abd)
print(type(abd))
print(abd[0])
print(abd[-1])
print(abd[2])
print(abd[0:1])
print(abd[0:2])
print(abd[::2])
print(abd[::3])
print(abd[::-1])


#code2
abc=[1,4,7,9,[2,3],[5,5],"marwa","zara",8]
print(abc[5])
print(abc[4][1])
print(abc[7])
print(abc.index(7))
print(abc.index(1))
print(abc.index(8))
print(len(abc))


#code3
num=[3,6,9,0,1,"marwa"]
del num[1]
print(num) # we can delete the data in list-data-structures

del num    #will completely delete 
print(num)

print(num.clear())

num.remove(6)
print(num)

num.remove('marwa')
print(num)

num.pop()
print(num)

num.pop(1)
print(num)






