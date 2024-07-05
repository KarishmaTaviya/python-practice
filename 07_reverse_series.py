print('\n\nUsing for loop')
n=100
# loop to print numbers 
for i in range(n,0,-1):
    print(i,end=" ")

print('\n\nUsing while loop')

N = 1
I = 100
while I >= N:
    if I % 10 > 0:
        print(I, end = " ")
    else:
        print(I)
    I -= 1
