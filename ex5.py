#2nd Program to demonstrate system defined exception
try:
    f=open('file1.txt',"a")
    f.write('hello world')
except FileNotFoundError:
    print('Unable to open file')
else:
    f.close()
    print('Written to file')
