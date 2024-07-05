from random import randrange,choice
from sys import maxsize
from time import ctime
from string import ascii_lowercase as lc
import re

a=randrange(3,10)
print('a: ',a)
print('Maxsize: ',maxsize)
b=randrange(maxsize)
print('Rmax: ',b)
print('ctime ex: ',ctime(100))
print('ctime: ',lc)
print('sequence ex: ',choice(lc))
llen=randrange(4,8)
print('llen: ',llen)
print(lc)
print('abc'.join(choice(lc) for j in range(llen)))

print('***'*10)

tlds=('com','edu','net','org','gov')
f=open('gendata.txt',"w")

for i in range(randrange(5,11)):
    dtint=randrange(maxsize)
    dtstr=ctime(dtint)
    llen=randrange(4,8)
    login=''.join(choice(lc) for j in range(llen))
    dlen=randrange(llen,13)
    dom=''.join(choice(lc) for j in range(dlen))
    print(dtstr,' :: ',login+'@'+dom+'.'+choice(tlds),dtint,'-',llen,'-',dlen)
    s=dtstr+' :: '+login+'@'+dom+'.'+choice(tlds)+str(dtint)+'-'+str(llen)+'-'+str(dlen)
    f.write(s+"\n")

f.close()
#temp='abc123'
temp='Tue Sep 28 09:37:52 1971  ::  uncci@tzrhzwwrsec.org 54878872 - 5 - 11'
res=re.search('\d+ - \d+ - \d+',temp)
print(res)
res=re.match('.+?(\d+ - \d+ - \d+)',temp).group(1)
print(res)