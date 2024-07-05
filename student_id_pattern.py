import re

#LANDLINE NUMBER
#str = '(1234)-123456'
#pat = '(\(\d{4}\))\-(\d{6})'

#STUDENT ID
str = '17BCA038'
pat = '1[7-9]B[C|CO|B][A|M]\d{3}'

#EMAIL ID
#str = 'abc@gmail.com'
#pat = '\w+\@[a-z]+\.com'

res = re.match(pat,str)

if(res):
    print('its a match')
else:
    print('no match')

