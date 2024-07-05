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
		print("\nRecord updated successfully\n")

def insertbyname(pos,city):
	with open("cities.bin","rb") as f1, open("cities1.bin","wb") as f2:
		data = f1.read(rl * (pos-1))
		f2.write(data)
		n = len(city)
		city = city + (rl-n) * " "
		city = city.encode()
		f2.write(city)
		data = f1.read()
		f2.write(data)

	os.remove("cities.bin")
	os.rename("cities1.bin","cities.bin")
	print("\nRecord inserted successfully\n")

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
		print("\nRecord deleted successfully\n")

def append():
	f = open("cities.bin","a+")
	city = input("Enter city name: ")
	cl = len(city)
	city = city + (rl - cl) * " "
	f.write(city)
	f.seek(5,0)
	city = f.read()
	f.close()
	print("\nRecord appended successfully\n")

while True:
	print("\n1.write data to file")
	print("2.Read data to file")
	print("3.Search by position")
	print("4.Search by city")
	print("5.Update city")
	print("6.Insert at position")
	print("7.Append city")
	print("8.delete city")
	print("0.Exit\n")

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
		pos = int(input("enter position : "))
		city = input("Enter city name to be inserted : ")
		insertbyname(pos,city)
	elif choice == 7:
		append()
	elif choice == 8:
		city = input("Enter which city you want to delete:")
		deleteCity(city)
	elif choice == 0:
		break 
