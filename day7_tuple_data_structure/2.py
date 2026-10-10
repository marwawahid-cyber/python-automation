abd=(1,3,7,[9,5,6],7,2)
print(bool(abd))
abd=(3,5,6)
print(bool(abd))


#how to convert from list to tuple
abd=[1,5,1,23]
print(type(abd))



#Nested tuple
my_tuple=("ABD",[8,5,4],(1,4,5))
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[1][1])
print(my_tuple[2])
print(my_tuple[2][2])


#DEL
abd=(1,5,6,9)
print(abd)
del abd
print(abd)
abd=(1,5,6,9)
print(abd[0])
del abd[0]


#Length
abd=(5,6,78,98)
print(abd)
print(len(abd))



