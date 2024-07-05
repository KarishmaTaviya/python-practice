#1st python program to demonstrate multiple system defined exceptions
try:
    name='abc'
    #print('hello world')
    Print('hello world')
    #print('hello : ',name)
    text=input('Enter Something....: ')
    #As input type ^D
except Exception as e:
    print('Error')
    print('Doc : ',e.__doc__)
    print('Message : ', e.__str__())
else:
    print(text)

