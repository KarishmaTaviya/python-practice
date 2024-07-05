#Fibonacci with recursion

def febo(n):
    if n<=1:
        return n
    else:
        return febo(n-2)+febo(n-1)

a=int(input('Enter a number : '))
print('Febonacci series is : ')

for i in range(a):
    print(febo(i),end=' ')
