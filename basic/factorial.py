num=int(input("enter a number: "))
n=1
if num<0:
        print("enter positive integer")
elif num==0:

        print("no fact")
else:
        for i in range(1,num+1):
                 n=n*i
        print(n)
