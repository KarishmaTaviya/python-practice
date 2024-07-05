from matplotlib import pyplot as plt
from matplotlib import pylab as plb


plb.figure(1)
plb.plot([1,2,3,4],[1,2,3,4])
plb.title('First graph using Matplotlib')
plb.ylabel('Y axis')
plb.xlabel('X axis')
plb.savefig('Chart 1')

'''
plb.figure(2)
plb.plot([1,4,2,3],[5,6,7,8,])
plb.figure(1)
plb.plot([5,6,10,3])
'''

plt.show()


