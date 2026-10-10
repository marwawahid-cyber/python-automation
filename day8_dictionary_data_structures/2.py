num={"uname":"marwa", "passwd":"123"}
print(num)
num.pop('passwd') # here pop will work as to remove something
print(num)

#POPITEM
print(num.popitem())
print(num)           #will remove randomly


#DELETE
cred={"uname":"ABDEALI","pass":"Abd@123","server1":"192.168.1.1"}
print(cred)
print(cred['server1'])
del cred['server1']
print(cred)          # we can delete everything we want using del

#CONVERT LIST TO DICTIONARY
abd1=['one','two','three']
print(abd1)
print(type(abd1))
abd2=[1,2,3]
print(abd2)
print(type(abd2))
mydata=zip(abd1,abd2)
print(dict(mydata))

#FROMKEYS
abd1=['a','e','i','o','u']
print(abd1)
values="vowel"
mydata=dict.fromkeys(abd1,values)
print(mydata)


