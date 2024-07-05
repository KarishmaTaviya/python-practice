#grade marks for students 

print('Specify your grades:')

python=int(input('Python - '))
dw=int(input('DW - '))
android=int(input('Android - '))
project=int(input('Project - '))

total = python+dw+android+project

print('Total is {}'.format(total))

if total>90:
    print('A+')
elif total>80 and total<=90:
    print('A')
elif total>70 and total<=80:
    print('A-')
elif total>60 and total<=70:
    print('B')
elif total>50 and total<=60:
    print('C')
elif total>40 and total<=50:
    print('Just Pass')
elif total<=40:
    print('You Failing bruv')
else:
    print('Enter proper marks')
