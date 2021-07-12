x=[[1,2,3],
   [4,5,6],
   [7,8,9]]

z=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        z[j][i]=x[i][j]
for i in z:
    print(i)
