from json import dumps, loads

stu={'15bca001':{'Name':'abc','city':'rajkot'},
     '15bca002':{'Name':'def','city':'morbi'}}

print('Student Dictionary:',stu)

#Converting python dictionary to JSON
j=dumps(stu)

print('Raw JSON: ',j)

#Converting JSON to python
l=loads(j)

print('Dictionary again: ',l)
