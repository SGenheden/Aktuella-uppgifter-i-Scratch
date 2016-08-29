import matplotlib.pylab as plt

import numpy as np

f = plt.figure(1,(6.694,5.028))
a = plt.axes([0,0,1,1])

grid = np.ones([362,482,3])

for i in range(482):
    for j in range(0,362,24):
        grid[j+1,i,:] = (0.67,0.67,0.67)
    #grid[361,i,:] = (0.67,0.67,0.67)
for i in range(362):
    for j in range(0,482,24):
        grid[i,j,:] = (0.67,0.67,0.67)
    #grid[i,481,:] = (0.67,0.67,0.67)

im = a.imshow(grid)
plt.axis('off')
im.axes.get_xaxis().set_visible(False)
im.axes.get_yaxis().set_visible(False)
f.savefig("grid.png",dpi=72,bbox_inches='tight', pad_inches = 0)
