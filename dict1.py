# Converting string into dictionary

# student="abc=23,def=34,ghi=45,jkl=25"
# student = student.split(",")
# temp=[]
# for i in student:
# 	temp.append(i.split("="))

# temp1 = dict(temp)
# for key,value in temp1.items():
# 	temp1[key] = int(value)
# print(dict(temp1))




# converting list into dictionary
# state=["Gujarat","Maharashtra","Tamilnadu","Rajsthan"]
# capital=["Gandhinagar","Mumbai","Chennai","Jaipur"]

# print(dict(zip(state,capital)))

# result = {}
# for i in range(len(state)):
# 	result[state[i]] = capital[i]

# print(result)


# result = dict(zip(state,capital))
# print(result)


# print(list(zip(state,capital,cities)))

# sort dictionary 

# fruits = {"Apple":50,"Grapes":40,"Banana":25,"Mango":90}
# print(fruits)
# # sorting on the basis of key
# fruits1 = sorted(fruits.items(),key=lambda x : x[0],reverse=True)
# print(fruits1)
# # sorting on the bais of value
# fruits2= sorted(fruits.items(),key=lambda x : x[1],reverse=True)
# print(fruits2)

# f3 = sorted(fruits.items(),key=lambda x : x[0],reverse=True)
# print(f3)

# Find out unique characters from the given string

#  BOOK
# B O K
# HELLO

# H : 1
# E : 1
# L : 2
# O : 1

# word = input("Enter word : ")
# charcount = {}
# for character in word:
# 	charcount[character] = charcount.get(character,0) + 1

# for key,value in charcount.items():
# 	if value==1:
# 		print(key)
# print(charcount)


# resturant = {"Gujarati":180,"Punjabi":250}

# print("*" * 50)
# print("Welcome to MY RESTURANT")
# print("*" * 50)
# name=input("Enter name : ")
# gcount=int(input("How many gujarati thalis?: "))
# pcount=int(input("How many punjabi thalis?: "))

# print("*" * 50)


# # Creating and printing ordered dictionary
# from collections import OrderedDict

# d = OrderedDict()
# # dictionary[key] = value
# d[10] = 'A'
# d[11] = 'B'
# d[12] = "C"
# d[13] = "D"

# for key,value in d.items():
# 	print(key,"-",value)

# print(d)
# print(type(d))


# # passing dictionary to function
# def func(fruits):
# 	for key,value in fruits.items():
# 		print(key,"-",value)


# fruits = {"Apple":50,"Grapes":40,"Banana":25,"Mango":90}
# func(fruits)

# students={}

# n=int(input("How many students?: "))

# for i in range(n):
# 	key = input("Enter name: ")
# 	value = int(input("Enter marks in python: "))
# 	students.update({key:value})

# name = input("Enter name of the student : ")
# marks = students.get(name,-1)

# if marks!=-1:
# 	print(marks)
# else:
# 	print(name," is not available")


# student = {"rno":1,"name":"abc","emailid":"abc@abc.com","phno":1231231231}
# print(student)
# student.update({"marks":111})
# print(student)




# student = {"rno":1,"name":"abc","emailid":"abc@abc.com","phno":1231231231}

# print(student)
# student.clear()
# print(student)
# for i in student.values():
# 	print(i,type(i))

# for i in student.keys():
# 	print(i,type(i))
# for i in student.items():
# 	print(i[0],"->",i[1])

# print(student)
# values = student.values()
# print(values,type(values))
# keys = student.keys()
# print(keys,type(keys))
# print(student)

# Rno-1
# Name-abc