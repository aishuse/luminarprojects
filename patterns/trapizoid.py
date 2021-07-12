n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(end=" ")
    # n=n-1
    for j in range(0,i+5):
        print("*",end=" ")
    print("\r")
