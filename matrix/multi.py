import numpy
import array as arr

import numpy as np

x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[11,22,33],
   [44,55,66],
   [77,88,99]]
print(np.dot(x,y))




z=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(x)):
   for j in range(len(y[0])):
      for k in range(len(y)):
         z[i][j]+=x[i][k]*y[k][j]

for i in z:
   print(i)