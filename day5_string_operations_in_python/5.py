#STRIP
#code1
abd ="*marwa*"
print(abd)
#print(abd.strip())   #it will consider space if present 
print(abd.strip('*'))

 
#code2
num="zara"
print(num.strip('z'))
print(num.strip('a'))


#code3
abc="haya noor islamabad"
print(abc.strip('islamabd'))
print(abc.strip('noor'))     #this one will not work


#code4
abg="fatima ali fatima"
print(abg.rstrip('fatima'))
print(abg.lstrip('fatima'))


