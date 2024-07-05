import re

str='MVM COLLEGE OF COMMERCE MANAGEMENT & IT'

res=re.split('\s',str,3)
print('Split result: ',res)

res=re.sub('\s','#',str,3)
print('Sub: ',res)


'''
#pat=re.compile('o.',re.I)
#pat='o.'

res=re.findall(pat,str)
res1=re.search(pat,str)
print('Findall : ', res)
print('Search: ', res1)
print('Search: ', res1.span())

for i in re.finditer(pat, str):
    s = i.start()
    e = i.end()
    #print('String match "%s" at %d:%d' % 
    (str[s:e], s, e))
    print('String: ',str[s:e],'start:end ',s,'
    :',e)
'''