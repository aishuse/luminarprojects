n=5

for i in range(0,n):
    for j in range(0,i):
        print(end=" ")

    for j in range(0,5-i):
        print("*",end=" ")


    print("\r")

for i in range(0, n+1):
    for j in range(0, 5-i):
        print(end=" ")

    for j in range(0, i):
        print("*", end=" ")

    print("\r")