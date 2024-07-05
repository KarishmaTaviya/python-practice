#swap values of two variables Multiplication and Division

print('enter two values')
a=int(input())
b=int(input())

print('a is ',a,'\nb is ',b)

a = a * b
b = a / b
a = a / b

print('after the swap:\na is ',a,'\nb is ',b)
