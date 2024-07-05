# import os
# rl = 20

# def write():
# 	file = input("Enter file name: ")
# 	f = open(file+".bin","ab")
# 	n = int(input("Enter hoe many record:- "))
# 	for i in range(n):
# 		data = input("Enter data:- ")
# 		dl = len(data)
# 		data = data + (rl-dl) * " "
# 		f.write(data.encode())
# 	f.close()

# def read():
# 	file = input("Enter file name: ")
# 	f = open(file+".bin","rb")
# 	data = f.read()
# 	print(data.decode())
# 	f.close()
# def count():
# 	file = input("Enter file name: ")
# 	f = open(file+".bin","rb")
# 	filesize = os.path.getsize(file+".bin")
# 	word = int(filesize/rl)
# 	print("numbre of word in this page:-",word)
# 	char = int(filesize)
# 	print("numbre of char in this page:-",char)
# 	lc=0
# 	for line in f:
# 		lc+=1
# 	print("numbre of line in this page:-",lc)



# while True:
# 	print("1.Write")
# 	print("2.read")
# 	print("3.count")
# 	print("0.Exit")
# 	ch = int(input("Enter ch:- "))

# 	if ch == 1:
# 		write()
# 	elif ch == 2:
# 		read()
# 	elif ch == 3:
# 		count()
# 	elif ch == 0:
# 		break
import os
rl = 20
def write():
	file = input("Enter file name:- ")
	f = open(file+".bin","wb")
	n = int(input("Enter how many recode:- "))
	for i in range(n):
		data = input("Enter data:- ")
		dl = len(data)
		data = data + (rl-dl) * " "
		f.write(data.encode())
	f.close()


def read():
	file = input("Enter file name:- ")
	f = open(file+".bin","rb")
	data = f.read()
	print(data.decode())
	f.close()


def count():
	file = input("Enter file name:- ")
	f = open(file+".bin","rb")
	filesize = os.path.getsize(file+".bin")
	word = int(filesize/rl)
	print(word)
	char = int(filesize)
	print(char)
	lc=0
	for line in f:
		lc+=1
	print(lc)

	
while True:
	print("1.write")
	print("2.read")
	print("3.count")
	print("0.exit")

	ch = int(input("Enter ch:- "))

	if ch == 1:
		write()
	elif ch == 2:
		read()
	elif ch == 3:
		count()
	elif ch == 0:
		break