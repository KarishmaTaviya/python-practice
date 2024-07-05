import re

str='MVM COLLEGE OF COMMERCE MANAGEMENT & IT'

res = re.sub('\s','#',str,3)
print('sub : ',res)

res = re.subn('\s','#',str)
print('subn : ',res)
print('subn : ',res[1])

str="Guido van Rossum \nTim peters \nAlex Martelli \nJust van Rossum"
res=re.findall(r'\w+(?= van Rossum)',str)
print(res)

str="sales@gmail.com \n postmaster@gmail.com \n eng@gmail.com \n noreply@gmail.com"
res=re.findall(r'(?m)^\s*(?!noreply|postmaster)(\w+)',str)
print('Mail : ', res)

str='yes? Yes. YES!!'
res=re.findall(r'(?i)yes',str)
print(res)
res=re.findall(r'yes',str,re.I)
print(res)


str="This line is the first \naother line \nthat line, it's the best"
res=re.findall(r'(?im)(^th[\w ]+)',str)
print(res)

str="Guido van Rossum \nTim peters \nAlex Martelli \nJust van Rossum"
res=re.findall(r'\w+(?= van Rossum)',str)
print(res)

#search vs. match & Greediness
str="Thu Feb 15 17:46:04 2007::abc@gmail.com::1171590364-6-8"
pat='\d+-\d+-\d+'
res=re.search(pat,str)
print('Search : ',res)
print('Search group: ',res.group())

res=re.match(pat,str)
print('Match: ',res)