#swap values of two variables without temporary variable

print('enter two values')
a=int(input())
b=int(input())

print('a is ',a,'\nb is ',b)

a, b = b, a

print('after the swap:\na is ',a,'\nb is ',b)
