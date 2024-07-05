#Program to demonstrate 'raise'
marks=int(input('Enter marks : '))
if marks<0:
    raise Exception('Marks cannot be less than 0')
else:
    print(marks)

