import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
#print(t)
# red dashes, blue squares and green triangles
plt.figure(1)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

#plt.plot([1, 2, 3, 4])
plt.plot([1, 2, 3, 4],[1, 4, 9, 16])
plt.figure(2)
plt.plot([1, 2, 3, 4],[1, 4, 9, 16],'ro')
#plt.ylabel('some numbers')

plt.figure(3)
marks=[60,56,50]
subject=['sub1','sub2','sub3']
plt.bar(subject, marks, width=0.2,color='blue')

plt.figure(4)
plt.pie(marks,labels=subject)
plt.show()
