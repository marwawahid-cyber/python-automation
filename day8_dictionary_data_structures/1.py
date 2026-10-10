abd={"uname": "marwa" , "passwd": "123"}
print(abd)
print(type(abd))
print(abd["uname"]) #how to access your values by key pairs
print(abd["passwd"])
print(abd.get('passwd')) #this will handle exception handling when the key is not found in the dictionary


#Assigment
person={"name":"marwa","age":"20","city":"islamabad","country":"pakistan"}
print(person)
print(person['name'])
person['name']='zara'
print(person)

#COPY
person1=person
print(person1)
print(id(person))  # assign memory allocation will be same 
print(id(person1))

person2=person.copy()
print(person2)
print(id(person2))
print(id(person))  # whenever we use copy cmnd, mem allocation will be different

print(person.keys())     # when we only want keys to print
print(person.values())   # when we only want values to print
print(person.items())    # when we only want items to print
print(person.clear())    # when we want to clear 
person['salary']=10000   #we can add something  
print(person)












