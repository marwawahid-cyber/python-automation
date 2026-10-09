#SPLIT
#code1
name="marwa wahid marwa"
print(name)
print(name.split())

#code2
num="zara ali  zara islamabad pakistan "
print(num.split('zara'))

#code3
path="/root/admin/abd.txt"
print(path)
path1=path.split('.txt')
print(path1)
print(path1[0])


#JOIN
#code1
abd="my name is haya sulayman"
print(abd.split())
mysplit=abd.split()
print(mysplit)
myjoint= ' '.join(mysplit)
print(myjoint)


#cpde2
abc="abdeali"
print('#'.join(abc))
print('\t'.join(abc))
print('\n'.join(abc))
