import numpy as np

x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[11,22,33],
   [44,55,66],
   [77,88,99]]

z=[[0,0,0],
   [0,0,0],
   [0,0,0]]

print(len(x[2]))
print(x[2])

print(np.add(x,y))

for i in range(len(x)):
   for j in range(len(x[0])):

      z[i][j]= x[i][j]+ y[i][j]


for i in z:
   print(i)