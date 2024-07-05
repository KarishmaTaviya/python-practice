import json

#Creating an object which is iterator of tuples
a=zip('abcde',range(5))

#creating a python dictionary
b=dict(a)

#Printing Values
print('a: ', a)
print(tuple(a))
print('b: ', b)

#Converting python dictionary to JSON
c=json.dumps(b)

#The result is JSON string
print('JSON string: ', c)

# some JSON:
j='{"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}'

#Parse JSON i.e. j
#Converting JSON to python
d=json.loads(j)

#The result is python dictionary
print('Python Dictionary: ',d)
print('Value of c: ',d["c"])

#print(json.loads(json.dumps(dict(zip('abc',range(3))))))

e=list('abcde')
print(e)

print(json.dumps(e))