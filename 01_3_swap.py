#swap values of two variables by Addition and Subtraction

print('enter two values')
a=int(input())
b=int(input())

print('before the swap:\na is ',a,'\nb is ',b)

a = a + b
b = a - b
a = a - b

print('after the swap:\na is ',a,'\nb is ',b)
