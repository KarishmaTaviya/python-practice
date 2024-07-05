#Program to demonstrate user defined exceptions
class InvalidMarks(Exception):
    def __init__(self,value):
        Exception.__init__(self)
        self.value=value

try:
    marks=int(input('Enter marks : '))
    if marks<0:
        raise InvalidMarks(0)   
except InvalidMarks as IM:
    print('Marks cannot be less than :  ',IM.value)
else:
    print(marks)
