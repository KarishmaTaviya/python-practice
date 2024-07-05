import os
rl = 20

#1st function to write the data 
def writeData():
	f =  open("cities.bin","ab")
	n = int(input("How many cities: "))
	for i in range(n):
		city = input("Enter city name: ")
		cl = len(city)
		city = city + (rl - cl) * " "
		f.write(city.encode())
	f.close()

def readData():
	f = open("cities.bin","rb")
	city = f.read()
	print(city.decode())
	f.close()

def searchByPosition(pos):
	f = open("cities.bin","rb")
	f.seek((pos-1)*rl,0)
	city = f.read(rl)
	print(city.decode())
	f.close()

def searchByCity(scity):
	f = open("cities.bin","rb")
	pos = 0
	filesize = os.path.getsize("cities.bin")
	n = int(filesize/rl)
	flag = 0
	for i in range(n):
		f.seek(pos)
		city = f.read(rl)
		if city.decode().strip().lower() == scity.lower():
			flag = 1
			break
		pos += rl
	f.close()
	return flag,(i+1)

def updateCity(city):
	flag,pos = searchByCity(city)
	if flag == 0:
		print("city dosen't Exist")
	else:
		#ncity =  input("Enter new city :")
		#print(pos)
		f = open("cities.bin","r+b")
		f.seek((pos-1)*rl)
		ncity =  input("Enter new city name : ")
		ncl = len(ncity)
		ncity = ncity + (rl - ncl) * " "
		f.write(ncity.encode())
		f.close()

def deleteCity(ncity):
	flag,pos = searchByCity(ncity)
	if flag == 0:
		print("City doesn't exist")
	else:
		filesize = os.path.getsize("cities.bin")
		n = int(filesize/rl)
		f1 = open("cities.bin","rb")
		f2 = open("ncity.bin","wb")
		for i in range(n):
			city = f1.read(rl)
			if city.decode().strip().lower() != ncity.lower():
				f2.write(city)
		f1.close()
		f2.close()
		os.remove("cities.bin")
		os.rename("ncity.bin","cities.bin")

while True:
	print("1.write data to file")
	print("2.Read data to file")
	print("3.Search by position")
	print("4.Search by city")
	print("5.Update city")
	print("6.delete city")
	print("7.Exit")

	choice =  int(input("Enter your choice: "))
	if choice == 1:
		writeData()
	elif choice == 2:
		readData()
	elif choice == 3:
		pos = int(input("Enter Position : "))
		searchByPosition(pos)
	elif choice == 4:
		city = input("enter city: ")
		flag,position = searchByCity(city)
		if flag == 0:
			print("city not found...")
		else:
			print("city found at position",position)
	elif choice == 5:
		city = input("Enter which city you want to update: ")
		updateCity(city)
	elif choice == 6:
		city = input("Enter which city you want to delete:")
		deleteCity(city)
	elif choice == 7:
		break 


# random access - binary file handling - all operations
reclen = 20
import os

def insertbyname():
	pos = int(input("enter position : "))
	country = input("Enter country name to be inserted : ")
	with open("countries.bin","rb") as f1, open("countries1.bin","wb") as f2:
		data = f1.read(reclen * (pos-1))
		f2.write(data)
		n = len(country)
		country = country + (reclen-n) * " "
		country = country.encode()
		f2.write(country)
		data = f1.read()
		f2.write(data)

	os.remove("countries.bin")
	os.rename("countries1.bin","countries.bin")
	print("Record inserted successfully")		



def deletebyname():
	cnm = input("Enter country name to delete: ")
	pos = searchbyname(cnm)
	if pos==-1:
		print("Reocrd can not be updated as it is not there in file")
	else:
		filesize = os.path.getsize("countries.bin")
		nor = int(filesize/reclen)
		with open("countries.bin","rb") as f1, open("countries1.bin","wb") as f2:
			pos = 0
			flag=0
			for i in range(nor):
				f1.seek(pos)
				country = f1.read(20)
				if country.decode().strip().lower()!=cnm.lower():
					f2.write(country)
				pos+=reclen
		os.remove("countries.bin")
		os.rename("countries1.bin","countries.bin")
		print("Record deleted successfully")		


def updatebyname():
	cnm = input("Enter country name to update: ")
	pos = searchbyname(cnm)
	if pos==-1:
		print("Reocrd can not be updated as it is not there in file")
	else:
		with open("countries.bin","r+b") as f:
			f.seek(pos)
			ncnm = input("Provide new name : ")
			n = len(ncnm)
			ncnm = ncnm + (reclen-n) * " "
			ncnm = ncnm.encode()
			f.write(ncnm)

def writedata():
	n = int(input("How many countries?: "))
	with open("countries.bin","wb") as f:
		for i in range(n):
			country = input("Enter country name : ")
			n = len(country)
			country = country + (reclen-n) * " "
			country = country.encode()
			f.write(country)
			# f.write(country+((reclen-len(country)) * " "))

def readalldata():
	with open("countries.bin","rb") as f:
		data = f.read()
		print(data.decode())

def searchbypos():
	n = int(input("Enter position: "))
	with open("countries.bin","rb") as f:
		f.seek(reclen * (n-1))
		country = f.read(20)
		print(country.decode())

def searchbyname(cnm):
	with open("countries.bin","rb") as f:
		filesize = os.path.getsize("countries.bin")
		nor = int(filesize/reclen)
		pos = 0
		flag=0
		for i in range(nor):
			f.seek(pos)
			country = f.read(20)
			if country.decode().strip().lower()==cnm.lower():
				flag=1
				print("Record found at : ",i+1)
				break
			pos+=reclen

		if flag==0:
			print("Record not found")
			pos=-1
			
	return pos





while True:
	print("1) Write data to file")
	print("2) Read all data from file")
	print("3) Search by position")
	print("4) Search by name")
	print("5) Update country")
	print("6) Delete country")
	print("7) Insert country")
	print("9) Exit")
	choice = int(input("Enter your choice : "))

	if choice==1:
		writedata()
	elif choice==2:
		readalldata()
	elif choice==3:
		searchbypos()
	elif choice==4:
		cnm = input("Enter country name : ")
		searchbyname(cnm)
	elif choice==5:
		updatebyname()
	elif choice==6:
		deletebyname()
	elif choice==7:
		insertbyname()
	elif choice==9:
		break


# to append data to an existing file and displaying the entire file.
# f = open("message.txt","a+")
# while True:
# 	data = input()
# 	if data=="*":
# 		break
# 	else:
# 		f.write(data+"\n")

# f.seek(5,0)
# data = f.read()
# print(data)
# f.close()