import os
rl = 20
fnm = "demo.txt"
def write():
	f = open(fnm,"ab")
	n = int(input("How many name: "))
	for i in range(n):
		name = input("Enter your name: ")
		nl = len(name)
		name = name + (rl-nl)* " "
		f.write(name.encode())
	f.close()

def read():
	f = open(fnm,"rb")
	name = f.read()
	print(name.decode())
	f.close()

def serachByPos():
	f = open(fnm,"rb")
	pos = int(input("position: "))
	f.seek((pos-1)*rl,0)
	name = f.read()
	print(name.decode())
	f.close()

def searchByCity(scity):
	f = open(fnm,"rb")

	pos,flag = 0
	filesize = os.path.getsize(fnm)
	n = int(filesize/rl)

	for i in range(n):
		f.seek(pos)
		name = f.read(rl)
		if name.decode().strip().lower()==scity.lower():
			flag = 1
			break
		pos += rl
	f.close()
	return flag,(i+1)


def update(city):
	flag,pos = searchByCity(city)
	if flag == 0:
		print("not found")
	else:
		f = open(fnm,"r+b")
		f.seek((pos-1)*rl)
		nname = input("Enter your name: ")
		nnl = len(nname)
		nname = nname + (rl-nl)* " "
		f.write(nname.encode())
		f.close()
		print("Done")

def insertAtPos(pos,name):
	f1 = open(fnm,"rb")
	f2 = open(fnm,"wb")
	data =  f1.read((pos-1)*rl)
	fr.write(data)
	n = len(name)
	name = name + (rl-n)* " "
	name = name.encode()
	fr.write(name)
	data = f1.read()
	fr.write(data)
	os.remove(fnm)
	os.rename(f1,f2)


def append():

def delete(nname):
	flag,pos = searchByCity(city)
	if flag == 0:
		print("not")
	else:
		filesize= os.path.getsize(fnm)
		n= int(filesize/rl)
		f1 = open(fnm,"rb")
		f2 = open(fnm,"wb")
		for i in range(n):
			name  = f1.read(rl)
			if city.decode().strip.lower()!=nname.lower():
				f2.write(name)
		f1.close()
		f2.close()
		os.remove(fnm)
		os.rename(f1,f2)



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

	ch = int(input("Enter your choice: "))
	if ch == 1:
		write()
	elif ch == 2:
		read()
	elif ch == 3:
		serachByPos()
	elif ch == 4:
		city = input("Enter city name: ")
		flag,pos = searchByCity(city)
		if(flag==0):
			print("Not found")
		else:
			print("found at",pos)
	elif ch == 5:
		name = input("update: ")
		update(name)
	elif ch == 6:
		pos = int(input("enter pos:"))
		name = input("enter name: ")
		insertAtPos(pos,name)
	elif ch == 7:
		append()
	elif ch == 8:
		name = input("enter name to delete: ")
		delete(name)
	elif ch == 0:
		read()