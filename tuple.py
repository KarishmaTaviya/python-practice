# students = (
# 			(1,"ABC",12,13,19),
# 			(2,"DEF",22,16,15),
# 			(3,"GHI",12,23,27),
# 			(4,"JKL",26,13,18),
# 			(5,"MNO",12,13,25)
# 			)
# 1) provoide rollno and whether that rno exist or not
# if exists print the details
# 2) provide markesheet of particular students - total, average
# 3) sorting - s1, s2, s3 - descending oreder



#sorting nested tuples
# a=((13,"Zabc",1234.56),
#    (11,"fdef",2300.00),
#    (12,"whi",3214.90))
# print(sorted(a,key=lambda x:x[2],reverse=True))
# print(sorted(a)) # sorted on the basis 1st element - ascending
# print(sorted(a,reverse=True)) # sorted on the basis 1st element - descending
# print(sorted(a,key=lambda x:x[1]))
# print(sorted(a,key=lambda x:x[1],reverse=True))

# print(sorted(a,key=lambda x :x[0],reverse=True))



# a = (1,2,3,4,(5,6),(7,8))
# print(a[5][1])
# # get values from user as tuple and display 
# # total and average
# numbers = eval(input("Enter elements in () : "))
# sum=0
# for i in numbers:
# 	sum+=i
# print(sum/len(numbers))
# print(sum(numbers))
# a = (1,2,3,2,1,1,1,2,2,1)
# print(a.index(2))
# print(a.count(1))

# print(1 in a)

# b = (4,5,6)
# print(a+b)
# a = (123,) * 4
# print(a)

# (123,123,123,123)

# a = (50,60,70,80,90,100)
# print(len(a))
# print(a[-4:-1]) #step value is 1

# print(a[-1])
# a = tuple(range(1,10,2))
# print(a,type(a))

# a = [1,2,3]
# print(a,type(a))
# b = tuple(a)
# print(b,type(b))
# a = 1,2,3,4
# print(a,type(a))



# deleting element from tuple
# names = ("abc","def","ghi","jkl")
# print(names)
# index=int(input("Enter index : "))
# result=names[0:index] + names[index+1:]
# print(type(result),result)




# modifying element into the tuple
# names = ("abc","def","ghi","jkl")
# index=int(input("Enter index : "))
# name =(input("Enter new name : "),)
# result=names[0:index] + tuple(name) + names[index+1:]
# print(type(result),result)

# 1st index def to defg

# inserting value into tuple
# names = ("abc","def","ghi","jkl")
# index=int(input("Enter index : "))
# name =(input("Enter Name : "),)
# result=names[0:index] + tuple(name) + names[index:]
# print(type(result),result)



# index = 2 #int(input("Enter position: "))
# name = tuple("temp",) #input("Enter name: ")


# result = names[0:index]
# result = result + name
# print(result)
# # result=[]
# # result.append(names[0:index])
# # print(result)

# # names = list(names)
# # names.insert(index,name)
# # print(tuple(names))

# # print(names,type(names))

# # index->2
# # name->temp

# # 0 to index-1 | "abc","def"
# # name         | "abc","def","temp"
# # index to end | "abc","def","temp","ghi","jkl"