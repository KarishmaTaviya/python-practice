import re

str='MVM COLLEGE OF COMMERCE MANAGEMENT & IT'

pat=re.compile('O.',re.I)
res=re.findall(pat,str)
print('Findall : ', res)

for i in re.finditer(pat, str):
    s = i.start()
    e = i.end()
    print('String match "%s" at %d:%d' % (str[s:e], s, e))

res = re.sub('\s','#',str,3)
print('sub : ',res)

res=re.split('\s',str,1)
print(res)


'''import re
#pat='\d+(\.\d*)?'
pat='(\(\d{1,4}\))-(\d{1,7})'
str='(0281)-2459021'
res=re.match(pat,str)
if re.match(pat,str):
    print('Number matches')
    print('Group 1: ', res.group(1))
    print('Group 2: ', res.group(2))
else:
    print('No Match')
'''