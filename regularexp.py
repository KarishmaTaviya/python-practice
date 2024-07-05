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

'''
str='East or west India is the best'

res=re.match('(.*?)es(.*)',str)

print(res)
print(res.group())


print(res.group(1))
print(res.group(2))

str1="abc@gmail.com"

if re.search('\w+@[a-z]+\.[a-z]{3}$',str1):
    print('True')
else:
    print('False')
num='1234'
ob=re.compile('^[0-9]{3}$')
print(ob.search('123'))

str2='Sachin is cricketer. sachin is batsman'

res=re.findall('(?i)sach',str2)

print(res)

tno='0281-1234567'

res=re.search
('(?P<Citycode>\d{4})-(?P<no>\d{7})', )

print(res)







#search vs. match & Greediness
str="Thu Feb 15 17:46:04 2007::
abc@gmail.com::1171590364-6-8"
pat='\d+-\d+-\d+'
res=re.search(pat,str)
print('Search : ',res)
print('Search Group: ', res.group())

res=re.match(pat,str)
print('Match : ',res)

pat='.+\d+-\d+-\d+'
res=re.match(pat,str)
print('Match .+ : ',res)
print('Match .+ Group(0): ',res.group())


pat='.+(\d+-\d+-\d+)'
res=re.match(pat,str)
print('Match .+ : ',res)
print('Match .+() Group(0): ',res.group(0))
print('Match .+ ()Group(1): ',re.match(pat,str).group(1))

pat='.+?(\d+-\d+-\d+)'
res=re.match(pat,str)
print('Match .+ : ',res)
print('Match .+?() Group(0): ',res.group(0))
print('Match .+?()Group(1): ',re.match(pat,str).group(1))



str='MVM COLLEGE OF COMMERCE MANAGEMENT & IT'

res = re.sub('\s','#',str,3)
print('sub : ',res)

res = re.subn('\s','#',str)
print('sub : ',res)

str="Guido van Rossum \nTim peters \nAlex Martelli \nJust van Rossum"
res=re.findall(r'\w+(?= van Rossum)',str)
print(res)

str=" sales@gmail.com \n postmaster@gmail.com \n eng@gmail.com \n noreply@gmail.com"
res=re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',str)
print('Mail : ', res)


str='yes? Yes. YES!!'
res=re.findall(r'(?i)yes',str)
print(res)

str="This line is the first \naother line \nthat line, it's the best"
res=re.findall(r'(?im)(^th[\w ]+)',str)
print(res)

str="Guido van Rossum \nTim peters \nAlex Martelli \nJust van Rossum"
res=re.findall(r'\w+(?= van Rossum)',str)
print(res)
'''
