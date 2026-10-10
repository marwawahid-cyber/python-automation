#setdefault
username={}
username.setdefault("username",'ABD')
print(username)
username.setdefault("password",'ABD@#134')
print(username)


#SORTED
cred={'username': 'ABD', 'password': 'ABD@#134'}
print(cred)
print(sorted(cred))
cred={'username': 'ABD', 'password': 'ABD@#134',"ABD":"abd"}
print(sorted(cred))


#How do i check if keys exists in a dictionary
cred={'username': 'ABD', 'password': 'ABD@#134'}
print(cred)

if "username" in cred:
    print(cred['username'])
    print("Data is present")
else:
    print("sorry your data is not available")



    #Nested dictionary:-
myinfo = {'username': 'ABD', 'password': 'ABD@#134'}

myinfo= {
1 : {'uname':'abd','pass':'ABD@123','server1':'Linux'},
2 : {'uname':'ali','pass':'ali@123','server1':'AIX'},
3 : {'uname':'kazim','pass':'kazim@123','server1':'windows'}
}
print(myinfo[1])
print(myinfo[2])
print(myinfo[3])
print(myinfo[3]['pass'])


#nested diction with list
myinfo = {
"server1" : ["192.168.1.1","192.168.1.2","192.168.1.3"],
"server2" : ["192.168.2.1","192.168.2.2","192.168.2.3"],
"server3" : ["192.168.3.1","192.168.3.2","192.168.3.3"]
}
print(myinfo)
print(myinfo['server2'])
print(myinfo['server2'][0])
print(myinfo['server2'][2])


