class Pen:
	def __init__(self,type="BallPoint",color="Red",company="XYZ"):
		self.type = type
		self.color = color
		self.company = company

	def display(self):
		print(self.type," ",self.color," ",self.company)


p1 = Pen()
p2 = Pen("Ink")
p3 = Pen("Ink","Blue")
p4 = Pen("Ink","Green","ABC")
p5 = Pen("Ink",company="ABC")

p1.display()
p2.display()
p3.display()
p4.display()
p5.display()


# # inner class
# class Employee:
# 	def __init__(self):
# 		self.eid = "E0001"
# 		self.enm = "ABC"

# 	def display(self):
# 		print(self.eid, " ",self.enm)

# 	class Address:
# 		def __init__(self):
# 			self.street = "Kalawad Road"
# 			self.city = "Rajkot"
# 			self.pin = 360005
# 			self.state = "Gujarat"

# 		def display(self):
# 			print(self.street," ",self.city," ",self.pin," ",self.state)

# e = Employee()
# e.display()
# a = Employee.Address()
# a.display()

# class Bank:

# 	def __init__(self,name):
# 		self.name = name
# 		self.amount = 0

# 	def deposit(self,amount):
# 		self.amount += amount
# 		return self.amount

# 	def withdraw(self,amount):
# 		self.amount -= amount
# 		return self.amount		

# name = input("Enter name  : ")
# b = Bank(name)

# while True:
# 	print("d-Deposit\nw-Withdrawal\ne-Exit")
# 	choice = input("Enter your choice : ")
# 	if choice=='e':
# 		break
# 	amount = float(input("Enter amount : "))

# 	if choice=='d':
# 		print(b.deposit(amount))
# 	else:
# 		print(b.withdraw(amount))






# class Employee:
# 	no_of_emp = 0 # class variable
# 	auto_increment_per = 0.20 # class variable

# 	def __init__(self,fnm="",desig="",dept="",salary=0.0):
# 		self.fnm = fnm  # instance varaible
# 		self.desig = desig# instance varaible
# 		self.dept = dept # instance varaible
# 		self.salary = salary # instance varaible
# 		Employee.no_of_emp += 1

# 	# instance method
# 	def printdetails(self):
# 		print(self.fnm," ",self.desig," ",self.dept," ",self.salary)

# 	# instance method
# 	def applyincrement(self):
# 		self.salary = self.salary + (self.salary * Employee.auto_increment_per)


# e1 = Employee("ABC","Jr. Manager","Sales",30000)
# e2 = Employee("DEF","Sr. Manager","Sales",45000)
# e1.printdetails()	
# e2.printdetails()
# e1.applyincrement()
# e2.applyincrement()
# e1.printdetails()	
# e2.printdetails()
# print("No. of employees are : ",Employee.no_of_emp)


# class MyClass:
# 	# instance method
# 	def instancemethod(self):
# 		return "instance method is called",self

# 	@classmethod
# 	def classmethod(cls):
# 		return "class method is called",cls

# 	@staticmethod
# 	def staticmethod():
# 		return "static method is called"

# m = MyClass()
# print(m.classmethod())
# print(m.staticmethod())
# print(m.instancemethod())


# print(MyClass.classmethod())
# print(MyClass.staticmethod())
# print(MyClass.instancemethod())



# static method example
# class Student:
# 	def __init__(self,rno,nm,m1,m2,m3):
# 		self.rno = rno
# 		self.nm = nm
# 		self.m1 = m1
# 		self.m2 = m2
# 		self.m3 = m3
# 	def printdetails (self):
# 		print(self.rno," ",self.nm," ",self.m1," ",self.m2," ",self.m3)

# class Result:
# 	@staticmethod
# 	def calculateResult(s):
# 		total = s.m1 + s.m2 + s.m3
# 		per = total/3.0
# 		print(total, " ",per)



# students = [] 
# students.append(Student(1,"abc",34,45,56))
# students.append(Student(2,"def",44,54,66))
# students.append(Student(3,"ghi",94,85,76))

# for i in range(len(students)):
# 	students[i].printdetails()
# 	Result.calculateResult(students[i])










# import math
# class Sample:

# 	@staticmethod
# 	def calculate(x):
# 		result = math.sqrt(x)
# 		return result

# no = float(input("Enter no. : "))
# result = Sample.calculate(no)
# print("Sqrt of {0} is {1}".format(no,result))



# # class method
# class Bird:
# 	wings = 2

# 	def __init__(self):
# 		self.x = 2

# 	@classmethod
# 	def fly(cls,name):
# 		print(abccls.wings)
		

# Bird.fly("Sparrow")
# Bird.fly("Pigeon")




# instance method - accessor method and mutator method
# name and marks
# class Student:
# 	def getName(self):
# 		return(self.nm)
# 	def setName(self,snm):
# 		self.nm = snm
# 	def getMarks(self):
# 		return(self.marks)
# 	def setMarks(self,smarks):
# 		self.marks = smarks


# n = int(input("How many students? : "))
# students=[]
# for i in range(n):
# 	nm = input("Enter name : ")
# 	marks = int(input("Enter marks : "))
# 	s = Student()
# 	s.setName(nm)
# 	s.setMarks(marks)
# 	students.append(s)

# for i in range(n):
# 	print(students[i].getName()," ",students[i].getMarks())



# class Temp:
# 	# x is a class level variable
# 	x = 10

# 	def __init__(self):
# 		# y is a instance variable
# 		self.y = 20


# t1 = Temp()
# t2 = Temp()

# print(Temp.x," ",t1.x," ",t2.x)

# Temp.x += 300

# print(Temp.x," ",t1.x," ",t2.x)


# t1 = Temp()
# t2 = Temp()

# print(Temp.x," ",t1.x," ",t2.x)

# t1.x += 100
# t2.x += 200

# print(Temp.x," ",t1.x," ",t2.x)



# print (Temp.x)
# t1 = Temp()
# print (t1.x)

# t1.x += 100

# print (Temp.x)
# print (t1.x)
