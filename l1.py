# -*- coding: utf-8 -*-
# learn https://zhuanlan.zhihu.com/p/20878530?refer=intelligentunit
# learn http://blog.csdn.net/yuan1125/article/details/69934785
# learn http://blog.csdn.net/baoqian1993/article/details/52116164
# learn 偏函数 
"""
Created on Wed Jul  5 21:56:29 2017

@author: t
"""

import numpy as np
import matplotlib.pyplot as plt
from functools import partial


cArray = np.array([[2, -1],[-1, 2]])
cMatrix = np.mat(cArray)
bArray = np.array([[0],[3]])
bMatrix = np.mat(bArray)


#print(np.dot(cArray, bArray))
#print(cMatrix * bMatrix) 


unbMatrix = np.linalg.solve(cMatrix, bMatrix)
print(unbMatrix)
unbMatrixForMatrixOperation = np.linalg.pinv(cMatrix) * bMatrix
print(unbMatrixForMatrixOperation)

fig = plt.figure(1)


plt.xticks(np.arange(-5,10, 0.5))
plt.yticks(np.arange(-5,10, 0.5))
plt.title("-x + 2y = 3;2x-y=0")
plt.axhline(y=0, c='black')
plt.axvline(x=0, c='black')
ax = plt.gca()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-3, 4)

#x,y = np.meshgrid
x = np.arange(-3, 5, 1)

y1 = 2 * x;
y2 = (3 + x ) /2

plt.plot(x, y1, color='red', linewidth=1.0, linestyle='-')
plt.plot(x, y2, color='blue', linewidth=1.0, linestyle='--')
plt.grid()



fig = plt.figure(2)


plt.xticks(np.arange(-5,10, 0.5))
plt.yticks(np.arange(-5,10, 0.5))
plt.title("")
plt.axhline(y=0, c='black')
plt.axvline(x=0, c='black')
plt.grid()

ax = plt.gca()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-3, 4)
x = np.arange(-3, 5, 1)

arrow_vector = partial(plt.arrow, width=0.01, head_width=0.1, head_length=0.2, length_includes_head=True)
arrow_vector(0, 0, cMatrix[0,0],cMatrix[1,0], color='g')
arrow_vector(0, 0, cMatrix[0,1], cMatrix[1,1], color='b')
arrow_vector(0, 0, bMatrix[0,0], bMatrix[1,0], color='r')
arrow_vector( 0 + cMatrix[0,0], 0 + cMatrix[1,0], cMatrix[1,0], cMatrix[1,1], color='y')
arrow_vector( 0 + cMatrix[0,0] + cMatrix[1,0], 0 + cMatrix[1,0] + cMatrix[1,1], cMatrix[1,0] , cMatrix[1,1], color='y')

plt.show()


