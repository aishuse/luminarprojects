n=5
k=5
for i in range(n,0,-1):
    for j in range(0,k):
        print(end=" ")
    k=k+1
    for j in range(0,i):
        print("* ",end="")
    print("\r")


