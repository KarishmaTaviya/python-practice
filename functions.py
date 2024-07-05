#def fun_name(parameters/arguments)

#without argument

def printline():
    for i in range(30):
        print(' ♡',end='')

printline()
print('\n Demo of functions')
printline()

#with default argument
print('\n')
def printline(ch,n=20):
    for i in range(n):
        print(ch,end='')

printline(' ❋')
print('\n Demo of functions')
printline(' ❋')


#with default argument
print('\n')
def printline(ch,n=20):
    for i in range(n):
        print(ch,end='')

printline(' ★')
print('\n Demo of functions')
printline(' ★')

#Demo of function with return value
print('\n')
def maxnum(x,y):
    if x>y:
        return x
    else:
        return y

x=int(input('Value of x :'))
y=int(input('Value of y :'))

print('The max num is :',maxnum(x,y))
