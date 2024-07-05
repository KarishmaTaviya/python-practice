
try:
    f=open('file2.txt','wt')
    f.write('Hello World')
except FileNotFoundError:
    print('Unable to find file ; ')
else:
    f.close()
    print('Text written to file')




#Example of user defined exception
class InvalidMarks(Exception):
    def __init__(self,value):
        Exception.__init__(self)
        self.value=value

try:
    marks=int(input('Enter marks : '))
    if marks<0:
        raise InvalidMarks(0)
except InvalidMarks as IM:
    print('Marks cannot be less than :  ',IM.value)
else:
    print(marks)


try:
    f=open("file1.txt",'wt')
    f.write('Hello World')
except FileNotFoundError:
    print('Unable to find the file')
else:
    f.close()
    print('Text written to file')

try:
    name='abc'
    print('hello : ',name)
    text=input('Enter Something....: ')
except NameError:
    print('Error: An identifier is not found')
except EOFError:
    print('Error : End of file found')
else:
    print(text)
'''
