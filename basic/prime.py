     #  PRIME NUMBER

n=int(input("enter a number: "))
for i in range(2,n):
    if n%i==0 :
        print(" not prime")

        break
else:
    print(" prime")



n = int(input("enter a limit: "))

for num in range(1,n):

    for i in range(2, num):
        if num % i == 0:
            break               # control goes to main for loop ie, for num in range(1,n):
    else:
        print(num ,end=" ")
#
# n = int(input("enter a limit: "))
# for i in range(1,n):
#     for x in range(2,i):
#         if i%x==0:
#             break
#     else:
#         print(i, end=" ")