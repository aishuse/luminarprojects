n=5

s=0
for i in range(0,n):
    for j in range(0,s+i):
        print(end=" ")

    for j in range(0,n):
        print("* " ,end="")
    print("\r")


n=5
s=0
for i in range(n,0,-1):
    for j in range(0,s+i):
        print(end=" ")

    for j in range(0,5):
        print("* " ,end="")
    print("\r")






