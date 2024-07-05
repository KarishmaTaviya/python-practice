#function that returns max and min of three


def maxofthree():
    lst=[]
    tot=int(input('How many numbers do you want to compare? '))
    print('Enter numbers :\n')
    for i in range(tot):
        num=int(input())
        lst.append(num)
        
    print('The numbers are : ',lst)
    print('\nThe maximum is : ',max(lst))
    print('\nThe minimum is : ',min(lst))
    
maxofthree()
