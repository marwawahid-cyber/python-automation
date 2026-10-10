abd=(1,3,7,9)
print(abd)
print(type(abd))



abc=(1)
print(abc)
print(type(abc))    #this will give class as int



#Slicing
abd=(1,3,7,[9,5,6],7,2)
print(abd)
print(abd[1])
print(abd[2])
print(abd[3])
print(abd[3][0])
print(abd[3][1])
print(abd[3][2])




abd=(1,3,7,[9,5,6],7,2)
print(abd[3][1])
print(abd[1])
abd[1]="ABD"   #this will give an error cuz tuple does not support item assignmet

abd[3][1]="ABD"
print(abd)


print(abd[-1])
print(abd[:-2])
print(abd[-2])
print(abd[-3])
print(abd[1:4])
print(abd[0:])
print(abd[:-1])
print(abd[:-2])
print(abd[:-3])
print(abd[::-1])
