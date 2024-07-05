import matplotlib.pylab as plb
import matplotlib.pyplot as plt

p=10000
r=0.05
years=20
values=[]

for i in range(years+1):
    values.append(p)
    p += p*r

plb.figure('fig1')
#plb.plot(values,color='blue',linewidth=5)
plb.plot(values,'k-.')
plb.title('5% growth compounded Annually')
plb.xlabel('Years of compounding')
plb.ylabel('Value of Principal')
plb.show()

