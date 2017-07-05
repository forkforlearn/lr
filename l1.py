# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:56:29 2017

@author: t
"""

import numpy as np
import matplotlib.pyplot as plt


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

fig = plt.figure()
ax = plt.subplots()

plt.xticks(np.arange(0,10))
plt.yticks(np.arange(0,10))
plt.axhline(y=0, c='red')
plt.axvline(x=0, c='black')
plt.plot(unbMatrixForMatrixOperation, color='red', linewidth=1.0, linestyle='--')
plt.grid()
plt.draw()
