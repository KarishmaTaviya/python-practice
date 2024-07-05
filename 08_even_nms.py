#Initialise variable with number of even numbers you want
n=int(input('Enter number : '))
 
#In the below example the syntax of for loop is as below for i in
#range(start,stop,step): start is the starting point for the range stop
#is until which number the range should belong to step is the number
#which you want to step by every time the statements gets looped
 
for num in range(2,n*2+1,2):
    print(num)
 
