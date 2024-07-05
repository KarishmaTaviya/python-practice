'''
#create a new file
f=open('student.txt','wt')
for i in range(10):
    st=input('Enter your full name : ')
    f.write(st+'\n')
f.close()

#open created file
f=open('student.txt','r')
for i in range(1):
    print(f.read())
f.close()
'''
#All names from ‘Student.txt’ file/Only first four names from the file
f=open('student.txt','r')
for i in range(10):
    print(f.readline(),end='')
f.close()
'''
#to print the file when you don't know the values of the files
f=open('names.txt','r')
for i in f:
    print(i,end='')
f.close()

f=open('student.txt','a')
for i in range():
    st=input('Enter name : ')
    f.write(st+'\n')
f.close()'''
