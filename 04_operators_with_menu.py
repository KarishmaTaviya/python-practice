'''Write a menu driven program to demonstrate the use of python
operators using the guidelines mentioned next. The level 1 menu must
allow the user to select the type of operators. Based on the type of
operators selected the next menu must display all the operators of that
type. In the third step accept the required numbers from the user and
demonstrate the operator selected by user. '''

print('Enter any two numbers')
a=int(input())
b=int(input())

print('\nMenu - Operators:\n1)Arithmetic\n2)Comparison\n3)Assignment\n4)Logical\n5)Bitwise\n')

choice=int(input('choose one - '))
#print(choice)

if choice==1:
    print("\nArithmetic Operators:\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Modulus\n6.Exponentiation\n7.Floor Division")
    print('\nthe values are: ',a,b)
    
    choice2=int(input('\nchoose one - '))
    
    if choice2==1:
        print('\nAddition - ',a+b)
        
    elif choice2==2:
        print('\nSubtraction - ',a-b)
    
    elif choice2==3:
        print('\nDivision - ',a/b)

    elif choice2==4:
        print('\nMultiplication',a*b)

    elif choice2==5:
        print('\nModulus',a%b)

    elif choice2==6:
        print('\nExponentiation',a**b)

    elif choice2==7:
        print('\nFloor Division',a//b)
    
    else :
        print('choose from the given menu')

    
elif choice==2:
    print("Comparison Operators:\n1.Equals\n2.Not Equals\n3.Greater Than\n4.Less Than\n5.Greater than or equal to\n6.Less than or equal to")
    print('\nthe values are: ',a,b)

    choice2=int(input('\nchoose one - '))
     
    if choice2==1:
        print('a=b : ',a==b)
        
    elif choice2==2:
        print('a!=b : ',a!=b)
    
    elif choice2==3:
        print('a>b : ',a>b)

    elif choice2==4:
        print('a<b : ',a<b)

    elif choice2==5:
        print('a>=b : ',a>=b)

    elif choice2==6:
        print('a<=b : ',a<=b)

    else :
        print('choose from the given menu')
        
elif choice==3:
    print("Assignment Operators:\n1. =\n2. +=\n3. -=\n4. *=\n5. /=\n6. %=\n7. //=\n8. **=")
    x=int(input('\nenter a value for variable x - '))

    choice2=int(input('\nchoose one - '))

    if choice2==1:
        y=x
        print('x=',y)
        
    elif choice2==2:
        x+=3
        print('x+=3 - ',x)
    
    elif choice2==3:
        x-=3
        print('x-=3 - ',x)

    elif choice2==4:
        x*=3
        print('x*=3 - ',x)

    elif choice2==5:
        x/=3
        print('x/=3 - ',x) 

    elif choice2==6:
        x%=3
        print('x%=3 - ',x)

    elif choice2==7:
        x//=3
        print('x//=3 - ',x)

    elif choice2==8:
        x**=3
        print('x**=3 - ',x) 

    else :
        print('choose from the given menu')
        
elif choice==4:
    print("Logical Operators:\n1.And\n2.Or\n3.Not")
    print('\nthe values are: ',a,b)

    choice2=int(input('\nchoose one - '))
    
    if choice2==1:
        print('a>b and b<a')
        print(a>b and b<a)
        
    elif choice2==2:
        print('a>b or b<a')
        print(a>b or b<a)
    
    elif choice2==3:
        print('not a>b')
        print(not a>b)
    
    else :
        print('choose from the given menu')
        
elif choice==5:
    print("Bitwise Operators:\n1. &\n2. |\n3. ^\n4. ~\n5. << left shift\n6. >> right shift")
    print('\nthe values are: ',a,b)

    choice2=int(input('\nchoose one - '))
     
    if choice2==1:
        print('a&b : ',a&b)
        
    elif choice2==2:
        print('a|b : ',a|b)
    
    elif choice2==3:
        print('a^b : ',a^b)

    elif choice2==4:
        print('~a : ',~a)

    elif choice2==5:
        print('a<<b : ',a<<b)

    elif choice2==6:
        print('a>>b : ',a>>b)

    else :
        print('choose from the given menu')
    
else:
    print("Invalid choice")

print('end')
