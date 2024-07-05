import re

psw='Hello Hellollo'

#Lookahead
res=re.search('Hello(?=llo)',psw)
print(res)

#Negative Lookahead
res=re.search('Hello(?!llo)',psw)
print(res)

#Lookbehind
res=re.search('(?<=Hello)llo',psw)
print(res)

#Negative Lookbehind
res=re.search('(?<!Hello)llo',psw)
print(res)
