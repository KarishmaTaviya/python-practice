import re
'''#str='abaabcd;aaa444efpqabefc999daaaa'
str='English-45; Maths-90; Science-80'
#print(str)
#pat='a{2,4}'
#pat='abc?'
pat='\W'
res=re.findall(pat,str)
print(res)



str='MVM COLLEGE OF COMMERCE MANAGEMENT & IT'
#pat='COL|COM'
#pat='COL[A-Z]{4}|COM'
#pat='CO[LM][A-Z]{4,5}'
pat='IT\Z'
#pat='OL{2}|OM{2}'
#pat='O[LM]'
res=re.findall(pat,str)
print(res)
'''
str='Sachin has a good bat.\nSachin is a good batsman. ' \
    '\nX has a good bat.'
print(str)
#pat='\ASachin'
#pat='\Bhin'
#pat='hin\b'
#pat='bat|bit'
#res=re.findall(pat,str)
res=re.findall(r'hin\b',str,re.M)
print(res)

str='MVM COLLEGE OF COMMERCE MANAGEMENT & IT'
res=re.search('o.', str,re.I)
print('Search Result : ', res)

str='MVM COLLEGE OF COMMERCE MANAGEMENT & IT'
res=re.match('.*college', str,re.I)
print('Match Result : ', res)
print('Match Result : ', res.group(0))

str='MVM COLLEGE OF COMMERCE MANAGEMENT & IT'
res=re.findall('O.', str,re.I)
print('Findall Result : ', res)

str='(2825)-245902'
pat='(\(\d{4}\))\-(\d{6})'
res=re.match(pat,str)
if re.match(pat,str):
    print('Number matches')
    print('group 1', res.group(1))
    print('group 1', res.group(2))
else:
    print('No Match')

str='Sachin has a good bat.\nSachin is a good batsman. ' \
    '\nX has a good bat.'
print(str)

res=re.findall(r'hin\b',str,re.M)
print(res)

res=re.findall(r'\bgoo',str,re.M)
print(res)