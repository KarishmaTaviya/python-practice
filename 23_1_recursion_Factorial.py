#Factorial with recursion

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

a=int(input('Enter a number : '))
f1=factorial(a)

print('The factorial of ',a,' is ',f1)
