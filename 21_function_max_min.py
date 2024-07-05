#function that returns max and min of three


def maxofthree():
    print('Enter three numbers :\n')
    a=int(input())
    b=int(input())
    c=int(input())
    print('The numbers are : ',a,' ',b,' ',c)

    print('\nThe maximum is : ',max(a,b,c))
    print('\nThe minimum is : ',min(a,b,c))
    
maxofthree()  
